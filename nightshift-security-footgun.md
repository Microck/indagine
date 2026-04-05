# Nightshift: Security Footgun Analysis — indagine

**Task:** security-footgun  
**Category:** analysis  
**Date:** 2025-04-05  

## Summary

Indagine is a meta-agent system that debugs other AI agents when they fail. It handles Azure credentials, Cosmos DB connections, and traces from external agent runs. The codebase has ~2,000 lines of Python across 30 files. This analysis identified 5 security-relevant findings, including 1 P1 and 2 P2 issues.

---

## Findings

### P1 — Critical

#### 1. Cosmos DB key passed directly via environment variable (cosmos_client.py:20,38)

```python
key = os.getenv("COSMOS_KEY", "").strip()
# ...
self._client = CosmosClient(url=settings.endpoint, credential=settings.key)
```

The Cosmos DB master key is read from an environment variable and stored as a plaintext attribute on the `CosmosSettings` dataclass. The key is a full account-level credential with read/write access to the entire Cosmos DB account.

**Risk:** If the process environment is leaked (error reports, logs, `/proc/PID/environ`), the entire database is compromised. The key is never rotated during the process lifetime.

**Recommendation:**
- Use Azure Managed Identity instead of a master key: `CosmosClient(url=endpoint, credential=DefaultAzureCredential())`
- The project already imports `azure.identity.DefaultAzureCredential` in `foundry_client.py` — reuse it here.
- If a key is unavoidable, use a key vault reference and resolve at runtime.

---

### P2 — High

#### 2. Foundry config falls back to YAML file with no encryption (foundry_client.py:26-31,46-48)

```python
def _read_yaml_defaults(config_path: Path) -> dict[str, Any]:
    data = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    return data if isinstance(data, dict) else {}
```

When `FOUNDRY_PROJECT_ENDPOINT` and `FOUNDRY_MODEL_DEPLOYMENT` env vars are not set, the code reads `infra/foundry_config.yaml`. If this file contains endpoint URLs or deployment names, they are stored in plaintext on disk. While the YAML appears to contain only non-secret endpoint info (not API keys), the pattern encourages users to add credentials there.

**Risk:** Plaintext config files may accumulate sensitive values over time. `yaml.safe_load` prevents code execution but not credential exposure.

**Recommendation:**
- Add a comment in the YAML template: `# Do NOT put API keys here. Use environment variables or Azure Key Vault.`
- Validate that the loaded config does not contain keys matching common credential patterns (e.g., `*_key`, `*_secret`, `*_token`).

#### 3. Traceback strings stored in failure metadata (failure_detector.py:152-156)

```python
metadata = {
    "exception_type": type(exc).__name__,
    "traceback": traceback.format_exc(),
}
```

Full Python tracebacks are captured and stored in `FailureEvent.metadata`. If these events are persisted to Cosmos DB (via `cosmos_client.upsert_trace_document`), tracebacks may contain:
- Local file paths
- Environment variable names
- Snippets of source code
- Variable values visible in the stack

**Risk:** Information leakage through persisted trace data. Other consumers of the Cosmos DB container can read detailed internal state.

**Recommendation:**
- Strip or redact the traceback before persistence. Keep only the exception type and message.
- Or: mark the metadata field as sensitive and ensure downstream consumers treat it accordingly.

---

### P3 — Medium

#### 4. `find_similar` protocol has no access control (diagnosis_engine.py:12-19)

The `_FixHistoryLookup` protocol accepts arbitrary `diagnosis` and `findings_report` objects without validation at the protocol level. The concrete implementation (`InMemoryFixHistory`) stores all past diagnoses in memory with no size bound.

**Risk:** An attacker who can control the findings report input could cause unbounded memory growth by submitting many unique diagnoses.

**Recommendation:** Add a max-size limit to `InMemoryFixHistory` and validate inputs at the protocol boundary.

#### 5. Fix proposals contain hardcoded file paths and code snippets (fix_generator.py)

All fix proposals (`_tool_misuse_fix`, `_hallucination_fix`, etc.) contain hardcoded `before` and `after` code snippets as strings. If these are applied to real source files without validation, they could:
- Patch the wrong file if paths change
- Insert code that doesn't match the actual source
- Create syntactically invalid files

**Risk:** Low in production (fixes are proposals, not auto-applied), but if the `unified_diff` output is fed to an automated patcher, it could corrupt source files.

**Recommendation:** Validate that the `before` string exists in the target file before applying any fix. Add a checksum or line-number anchor.

---

## Architecture Security Notes

### Positive findings

1. **`yaml.safe_load`** is used correctly (foundry_client.py:30) — prevents arbitrary code execution via YAML deserialization.
2. **Pydantic validation** is used throughout (models are validated with `model_validate`) — prevents malformed input from propagating.
3. **`dotenv` loaded with `override=False`** (foundry_client.py:38) — existing env vars take precedence over `.env` file, preventing local `.env` from overriding production credentials.
4. **No hardcoded credentials** — all secrets come from environment variables.

### Missing security controls

| Control | Status |
|---------|--------|
| Secret rotation | Not implemented |
| Input sanitization on trace data | Not implemented |
| Rate limiting on Cosmos writes | Not implemented |
| Audit logging | Not implemented |
| TLS verification for Azure clients | Default (handled by SDK) |

---

## Recommendations Summary

| Priority | Finding | Effort |
|----------|---------|--------|
| P1 | Cosmos key → Managed Identity | Medium |
| P2 | YAML config credential guard | Low |
| P2 | Traceback redaction before persistence | Low |
| P3 | InMemoryFixHistory size limit | Low |
| P3 | Fix proposal validation | Medium |
