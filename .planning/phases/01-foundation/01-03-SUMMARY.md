---
phase: 01-foundation
plan: "03"
subsystem: api
tags: [python, pydantic, opentelemetry, azure-cosmos, trace-storage]

requires:
  - phase: 01-01
    provides: Foundry/tracing scaffolding and shared runtime conventions
  - phase: 01-02
    provides: Deterministic failing subject scenarios with stable output contracts
provides:
  - FailureEvent + TraceRecord contracts for downstream analyzers
  - Failure detection wrapper with timeout, validation, exception, and hallucination classification
  - TraceStore persistence/retrieval API with Cosmos backend and in-memory fallback
  - End-to-end run/capture script that emits traces and retrieval summaries
affects: [02-analysis-pipeline, 03-diagnosis-fixes]

tech-stack:
  added: []
  patterns:
    [strict pydantic contracts with extra=forbid, failure-id keyed trace persistence, memory-first local verification path]

key-files:
  created:
    - src/models/__init__.py
    - src/models/failure.py
    - src/models/trace_record.py
    - src/core/failure_detector.py
    - src/storage/cosmos_client.py
    - src/storage/trace_store.py
    - src/scripts/run_and_capture.py
    - tests/test_trace_store_memory.py
  modified: []

key-decisions:
  - "Pinned TraceRecord to schema_version=1 with forbidden extras to lock analyzer-facing contract stability."
  - "Used failure_id as Cosmos partition key to keep get_trace(failure_id) read-item retrieval constant-time."

patterns-established:
  - "run_with_failure_detection returns a typed FailureEvent plus JSON-serializable TraceRecord payload."
  - "TraceStore defaults to in-memory when Cosmos env is absent, enabling local end-to-end execution."

duration: 9 min
completed: 2026-02-11
---

# Phase 1 Plan 3: Failure Detection and Trace Persistence Summary

**Failure detection now emits structured events and schema-pinned traces that can be persisted/retrieved by failure_id across memory and Cosmos store modes.**

## Performance

- **Duration:** 9 min
- **Started:** 2026-02-11T01:21:16Z
- **Completed:** 2026-02-11T01:30:57Z
- **Tasks:** 3
- **Files modified:** 8

## Accomplishments
- Added strict `FailureEvent` and `TraceRecord` models (schema version pinned to 1) for durable analyzer inputs.
- Implemented `run_with_failure_detection` to classify `validation_error`, `exception`, `timeout`, and `hallucination_flag` with captured trace steps.
- Implemented `TraceStore` with Cosmos + in-memory backends and added memory roundtrip tests.
- Added `run_and_capture` script that configures tracing, runs all subjects, stores traces, retrieves by `failure_id`, and prints JSON summaries.

## Task Commits

Each task was committed atomically:

1. **Task 1: Define FailureEvent model + failure detection wrapper** - `06c7231` (feat)
2. **Task 2: Implement TraceStore with Cosmos backend + in-memory fallback** - `69e0a9f` (feat)
3. **Task 3: Add one end-to-end script: run subject -> detect failure -> persist -> retrieve** - `39ecac9` (feat)

**Plan metadata:** Pending (created in docs commit after summary/state updates)

## Files Created/Modified
- `src/models/failure.py` - Defines the structured failure contract consumed by storage and analyzers.
- `src/models/trace_record.py` - Defines schema-versioned trace payload and step contract with forbidden extras.
- `src/core/failure_detector.py` - Wraps subject execution with timeout/error/hallucination classification and trace-step emission.
- `src/storage/cosmos_client.py` - Adds Cosmos configuration loading and trace document upsert/read operations.
- `src/storage/trace_store.py` - Adds store/get API with memory fallback and backend auto-selection.
- `src/scripts/run_and_capture.py` - End-to-end entrypoint for run, detect, persist, and retrieve flow.
- `tests/test_trace_store_memory.py` - Verifies in-memory roundtrip behavior and fallback semantics.

## Decisions Made
- Trace payload contract is enforced via Pydantic `extra="forbid"` to prevent hidden schema drift before Phase 2 analyzers depend on it.
- Trace retrieval API is keyed by `failure_id` and uses `failure_id` partitioning in Cosmos backend to keep read-path lookup direct.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] System Python lacked required modules for mandated `python3` verify commands**
- **Found during:** Task 1/Task 2/Task 3 verification
- **Issue:** `python3` environment could not import required modules (`opentelemetry`, `pytest`), causing verify command failures unrelated to repository code.
- **Fix:** Re-ran the same verification checks through the project virtualenv (`.venv/bin/python ...`) where plan dependencies are installed.
- **Files modified:** None (execution environment only)
- **Verification:** Detector contract check passed, full pytest suite passed, and end-to-end run/capture passed using memory backend.
- **Committed in:** N/A (no repository file change)

---

**Total deviations:** 1 auto-fixed (1 blocking)
**Impact on plan:** No scope change; deviation affected execution runtime only.

## Authentication Gates
None.

## Issues Encountered
None.

## User Setup Required

Cosmos-backed verification still requires Azure Cosmos credentials:
- `COSMOS_ENDPOINT`
- `COSMOS_KEY`
- `COSMOS_DATABASE`
- `COSMOS_CONTAINER_TRACES`

Once configured, run:

```bash
.venv/bin/python -m src.scripts.run_and_capture --store cosmos
```

## Next Phase Readiness
- Ready for `02-01-PLAN.md`: failure events and trace records are now durable inputs for analyzers.
- Cosmos execution path is implemented but awaits user-provided Cosmos environment values for live verification.

---
*Phase: 01-foundation*
*Completed: 2026-02-11*

## Self-Check: PASSED

- Verified key output files exist on disk.
- Verified task commits exist in git history: `06c7231`, `69e0a9f`, `39ecac9`.
