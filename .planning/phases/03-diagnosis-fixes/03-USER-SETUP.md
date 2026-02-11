# Phase 3: User Setup Required

**Generated:** 2026-02-11
**Phase:** 03-diagnosis-fixes
**Status:** Incomplete

Complete these items for fix-history similarity linking to Cosmos DB. Claude automated all repository code changes; the remaining items require Azure Portal access.

## Environment Variables

| Status | Variable | Source | Add to |
|--------|----------|--------|--------|
| [ ] | `COSMOS_ENDPOINT` | Azure Portal -> Cosmos DB account -> Keys -> URI | `.env.local` |
| [ ] | `COSMOS_KEY` | Azure Portal -> Cosmos DB account -> Keys -> PRIMARY KEY | `.env.local` |
| [ ] | `COSMOS_DATABASE` | Existing Cosmos database used for traces | `.env.local` |
| [ ] | `COSMOS_CONTAINER_FIXES` | Choose fix-history container name (for example `fixes`) | `.env.local` |

## Account Setup

- [ ] **Ensure Cosmos DB account access is available**
  - URL: https://portal.azure.com/
  - Skip if: You already manage the Cosmos account used by this project

## Dashboard Configuration

- [ ] **Create or confirm fix-history container**
  - Location: Azure Portal -> Cosmos DB account -> Data Explorer -> `COSMOS_DATABASE`
  - Set to: Container ID matching `COSMOS_CONTAINER_FIXES` (for example `fixes`)
  - Notes: Partition key should be `/failure_id` to match application writes

## Local Development

- Add the four variables above to your local `.env.local` (or `.env`) before running Cosmos-backed fix history.
- If you want memory-only mode, leave one or more `COSMOS_*` values unset and backend auto-selection will fall back to memory.

## Verification

After completing setup, verify with:

```bash
.venv/bin/python -m pytest -q
```

Expected results:
- Tests pass.
- `FixHistory()` auto-selects Cosmos when all four `COSMOS_*` values are present.

---

**Once all items complete:** Mark status as "Complete" at top of file.
