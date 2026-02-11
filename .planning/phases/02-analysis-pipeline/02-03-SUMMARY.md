---
phase: 02-analysis-pipeline
plan: "03"
subsystem: analysis
tags: [python, orchestration, findings-report, pipeline, pytest]

requires:
  - phase: 02-01
    provides: TraceAnalyzer output contracts and trace fixtures
  - phase: 02-02
    provides: ToolAnalyzer misuse detection and SchemaRegistry-based validation
provides:
  - AutopsyController orchestration entrypoint that runs TraceAnalyzer and ToolAnalyzer
  - Unified FindingsReport keyed by analyzer name for downstream diagnosis
  - AutopsyPipeline glue that loads trace by failure_id from injected TraceStore backend
affects: [02-analysis-pipeline, 03-diagnosis-fixes]

tech-stack:
  added: []
  patterns:
    [controller-level analyzer orchestration, injected-store pipeline wiring, unified findings envelope keyed by analyzer]

key-files:
  created:
    - src/core/autopsy_controller.py
    - src/core/autopsy_pipeline.py
    - tests/test_autopsy_controller.py
  modified: []

key-decisions:
  - "Findings are namespaced as trace_analyzer/tool_analyzer with list payloads to stay compatible with FindingsReport typing."
  - "AutopsyPipeline delegates backend/env selection to TraceStore helpers instead of parsing Cosmos settings directly."

patterns-established:
  - "AutopsyController exposes run_autopsy(trace_record) as the stable diagnosis entrypoint for analyzer orchestration."
  - "AutopsyPipeline accepts injected TraceStore and reads trace_record from get_trace(failure_id) before controller execution."

duration: 3 min
completed: 2026-02-11
---

# Phase 2 Plan 3: Autopsy Controller Orchestration Summary

**AutopsyController now converts stored traces into a unified FindingsReport by orchestrating TraceAnalyzer and ToolAnalyzer through a stable controller and pipeline entrypoint.**

## Performance

- **Duration:** 3 min
- **Started:** 2026-02-11T02:24:41Z
- **Completed:** 2026-02-11T02:28:36Z
- **Tasks:** 2
- **Files modified:** 3

## Accomplishments
- Added `src/core/autopsy_controller.py` with `run_autopsy(trace_record)` and `AutopsyController` orchestration over trace/tool analyzers.
- Added `src/core/autopsy_pipeline.py` as a thin injected-store pipeline (`failure_id -> TraceStore.get_trace -> run_autopsy`).
- Added `tests/test_autopsy_controller.py` integration coverage for unified report shape, SearchAgent tool-issue detection, and injected-store pipeline wiring.

## Task Commits

Each task was committed atomically:

1. **Task 1: Build AutopsyController orchestration API** - `39e9719` (feat)
2. **Task 2: Add integration test for unified FindingsReport shape** - `8756fc7` (test)

**Plan metadata:** Pending (created after summary/state updates)

## Files Created/Modified
- `src/core/autopsy_controller.py` - Controller API that runs analyzers and returns one unified `FindingsReport`.
- `src/core/autopsy_pipeline.py` - Pipeline glue for loading traces from an injected `TraceStore` and invoking controller orchestration.
- `tests/test_autopsy_controller.py` - Integration tests validating output shape and SearchAgent misuse findings.

## Decisions Made
- Used explicit analyzer keys (`trace_analyzer`, `tool_analyzer`) in `FindingsReport.findings` to keep outputs stable and diagnosable.
- Kept backend/env selection in `TraceStore` by introducing thin `create_trace_store`/`create_autopsy_pipeline` helpers instead of duplicating config parsing.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] System Python lacks pytest for required verification command**
- **Found during:** Task 2 verification and plan-level verification
- **Issue:** `python3 -m pytest -q` fails with `No module named pytest` in this environment.
- **Fix:** Ran the equivalent verification commands with project virtualenv: `.venv/bin/python -m pytest -q`.
- **Files modified:** None (execution environment only)
- **Verification:** `.venv/bin/python -m pytest -q` passed (`18 passed`).
- **Committed in:** N/A (no repository file change)

---

**Total deviations:** 1 auto-fixed (1 blocking)
**Impact on plan:** No scope change; deviation was runtime selection only.

## Authentication Gates
None.

## Issues Encountered
None.

## User Setup Required
None - no external service configuration required.

## Next Phase Readiness
- Phase 2 analysis pipeline goals are complete; ready to start `03-01-PLAN.md` diagnosis taxonomy implementation.
- Environment caveat remains: use `.venv/bin/python -m ...` for deterministic verification in this workspace.

---
*Phase: 02-analysis-pipeline*
*Completed: 2026-02-11*

## Self-Check: PASSED

- Verified key output files exist on disk.
- Verified task commits exist in git history: `39e9719`, `8756fc7`.
