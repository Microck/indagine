# Phase 1: User Setup Required

**Generated:** 2026-02-11
**Phase:** 01-foundation
**Status:** Incomplete

Complete these items for Azure AI Foundry verification and tracing. Code scaffolding is done; these values require your Azure account access.

## Environment Variables

| Status | Variable | Source | Add to |
|--------|----------|--------|--------|
| [ ] | `FOUNDRY_PROJECT_ENDPOINT` | Azure AI Foundry portal -> Project settings -> Endpoint | `.env` |
| [ ] | `FOUNDRY_MODEL_DEPLOYMENT` | Azure AI Foundry portal -> Models -> Deployments -> Deployment name | `.env` |
| [ ] | `APPLICATIONINSIGHTS_CONNECTION_STRING` (optional) | Azure Portal -> Application Insights -> Connection string | `.env` |

## Account Setup

- [ ] **Authenticate with Azure for local CLI access**
  - Command: `az login`
  - Alternative for CI/non-interactive: set `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET` in your shell/secret store

## Dashboard Configuration

- [ ] **Ensure Foundry project access is granted**
  - Location: Azure AI Foundry -> Project -> Access control (IAM)
  - Requirement: your identity (or service principal) can read project and deployment metadata

- [ ] **Verify model deployment exists**
  - Location: Azure AI Foundry -> Models -> Deployments
  - Requirement: deployment name matches `FOUNDRY_MODEL_DEPLOYMENT`

## Verification

After completing setup, verify with:

```bash
source .venv-plan01/bin/activate
python3 -m src.scripts.verify_foundry --strict
```

Expected results:
- Script prints resolved Foundry endpoint and deployment
- Tracing exporter path is printed (`azure-monitor` when telemetry is configured, otherwise `console`)
- Output includes `OK: deployment reachable: ...`

---

**Once all items complete:** Mark status as "Complete" at top of file.
