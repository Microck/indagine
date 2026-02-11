---
phase: 03-diagnosis-fixes
plan: "03"
subsystem: storage
tags: [python, azure-cosmos, diagnosis-engine, fix-history, pytest]

requires:
  - phase: 03-01
    provides: Deterministic diagnosis taxonomy output used as similarity query input
  - phase: 03-02
    provides: Fix proposal contract persisted by fix-history backends
provides:
  - In-memory and Cosmos-backed fix-history storage with similarity lookup by root_cause + sub_type
  - DiagnosisEngine wiring that always emits similar_past_failure_ids and derived count
  - User setup checklist for Cosmos fix-history container and environment variables
affects: [03-diagnosis-fixes, 04-demo-submit]

tech-stack:
  added: []
  patterns: [dual-backend fix history with auto fallback, diagnosis-to-history similarity lookup]

key-files:
  created:
    - src/storage/fix_history.py
    - src/storage/fix_history_memory.py
    - tests/test_fix_history_memory.py
    - .planning/phases/03-diagnosis-fixes/03-USER-SETUP.md
  modified:
    - src/core/diagnosis_engine.py

key-decisions:
  - "FixHistory uses backend='auto' semantics: Cosmos when all COSMOS_* fix-history vars exist, otherwise memory."
  - "DiagnosisEngine links past failures through FixHistory.find_similar(...) and defaults to empty links when history is unavailable."

patterns-established:
  - "Fix-history records are keyed by failure_id and indexed by root_cause/sub_type for deterministic similarity lookups."
  - "Similarity count remains derived from similar_past_failure_ids, preserving DIAG-04 consistency guarantees."

duration: 6 min
completed: 2026-02-11
---

# Phase 3 Plan 3: Fix History Similarity Wiring Summary

**Fix-history storage now supports memory and Cosmos backends, and DiagnosisEngine links prior matching failures through deterministic taxonomy/sub-type similarity queries.**

## Performance

- **Duration:** 6 min
- **Started:** 2026-02-11T04:25:37Z
- **Completed:** 2026-02-11T04:32:22Z
- **Tasks:** 2
- **Files modified:** 5

## Accomplishments
- Added `FixHistory` persistence in `src/storage/fix_history.py` with auto backend selection and Cosmos container support via `COSMOS_CONTAINER_FIXES`.
- Added `InMemoryFixHistory` in `src/storage/fix_history_memory.py` with `record_failure`, `record_fix`, and `find_similar` for local/dev usage.
- Added `tests/test_fix_history_memory.py` to validate similarity ID matching and limit behavior.
- Wired `src/core/diagnosis_engine.py` to query fix history and populate `similar_past_failure_ids` / `similar_past_failures` consistently.

## Task Commits

Each task was committed atomically:

1. **Task 1: Implement FixHistory store (memory + Cosmos) with a simple similarity query** - `b568e61` (feat)
2. **Task 2: Wire DiagnosisEngine to populate similar_past_failures** - `b4e93bd` (feat)

**Plan metadata:** Pending (created after summary/state/roadmap updates)

## Files Created/Modified
- `src/storage/fix_history.py` - Cosmos + memory-backed FixHistory facade with similarity lookup contract.
- `src/storage/fix_history_memory.py` - In-memory fix-history backend for tests/local dev.
- `tests/test_fix_history_memory.py` - Similarity lookup contract tests for match semantics and limits.
- `src/core/diagnosis_engine.py` - DiagnosisEngine dependency injection and similarity lookup wiring.
- `.planning/phases/03-diagnosis-fixes/03-USER-SETUP.md` - Human setup checklist for Cosmos fix-history configuration.

## Decisions Made
- Kept fix-history backend selection consistent with trace storage by using an `auto` mode that prefers Cosmos only when complete credentials are present.
- Moved diagnosis similarity linkage to explicit store lookup instead of inferring IDs from analyzer payload internals.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] System Python lacks pytest for required verification command**
- **Found during:** Task 1, Task 2, and plan-level verification
- **Issue:** `python3 -m pytest -q` failed with `No module named pytest` in this environment.
- **Fix:** Re-ran required verification using project virtualenv: `.venv/bin/python -m pytest -q`.
- **Files modified:** None (runtime environment only)
- **Verification:** `.venv/bin/python -m pytest -q` passed (`46 passed`).
- **Committed in:** N/A (no repository file changes)

---

**Total deviations:** 1 auto-fixed (1 blocking)
**Impact on plan:** No scope change; deviation only changed the Python runtime used for verification.

## Authentication Gates
None.

## Issues Encountered
None.

## User Setup Required

**External services require manual configuration.** See [03-USER-SETUP.md](./03-USER-SETUP.md) for:
- Environment variables to add
- Azure Portal container setup steps
- Verification command

## Next Phase Readiness
- Phase 3 is complete (3/3 plans); DIAG-01..DIAG-04 and FIX-01..FIX-04 implementation tracks are now covered.
- Ready for `04-01-PLAN.md` in `04-demo-submit`.
- Live Cosmos-backed verification remains dependent on user-provided credentials, now including `COSMOS_CONTAINER_FIXES` for fix-history lookup.

---
*Phase: 03-diagnosis-fixes*
*Completed: 2026-02-11*

## Self-Check: PASSED

- Verified output files exist: `src/storage/fix_history.py`, `src/storage/fix_history_memory.py`, `tests/test_fix_history_memory.py`, `.planning/phases/03-diagnosis-fixes/03-03-SUMMARY.md`, `.planning/phases/03-diagnosis-fixes/03-USER-SETUP.md`.
- Verified task commits exist in git history: `b568e61`, `b4e93bd`.
