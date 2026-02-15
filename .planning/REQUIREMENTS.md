# Requirements

## v1 Requirements

### Foundation (FOUND)

- [x] **FOUND-01**: Foundry project initialized with tracing enabled
- [x] **FOUND-02**: BookingAgent that can fail on date format parsing
- [x] **FOUND-03**: SearchAgent that can fail on wrong tool selection
- [x] **FOUND-04**: SummaryAgent that can hallucinate information
- [x] **FOUND-05**: Failure Detector that watches for exceptions, validation failures, timeouts
- [x] **FOUND-06**: Trace capture stores execution traces to Cosmos DB *(implementation complete; live Cosmos run pending credentials)*

### Analysis (ANLZ)

- [x] **ANLZ-01**: Trace Analyzer parses execution traces and identifies failure step
- [x] **ANLZ-02**: Trace Analyzer extracts reasoning chain that led to failure
- [x] **ANLZ-03**: Tool Analyzer validates parameters against tool schema
- [x] **ANLZ-04**: Tool Analyzer detects wrong tool selection
- [x] **ANLZ-05**: Indagine Controller orchestrates Trace and Tool analyzers
- [x] **ANLZ-06**: Indagine Controller collects findings into structured output

### Diagnosis (DIAG)

- [x] **DIAG-01**: Diagnosis Engine implements 6-type failure taxonomy
- [x] **DIAG-02**: Diagnosis Engine identifies root cause from analyzer findings
- [x] **DIAG-03**: Diagnosis Engine provides explanation of what went wrong
- [x] **DIAG-04**: Diagnosis Engine links to similar past failures (if any)

### Fixes (FIX)

- [x] **FIX-01**: Fix Generator proposes PROMPT_FIX changes (add instructions/examples)
- [x] **FIX-02**: Fix Generator proposes TOOL_CONFIG_FIX changes (add validation/transformation)
- [x] **FIX-03**: Fix Generator proposes GUARDRAIL_FIX changes (add output validation/retry)
- [x] **FIX-04**: Fix Generator shows exact diff of proposed changes

### Demo (DEMO)

- [x] **DEMO-01**: Scripted demo scenario with BookingAgent date format failure
- [ ] **DEMO-02**: 2-minute video showing: failure → analysis → diagnosis → fix suggestion *(manual recording/upload pending)*
- [x] **DEMO-03**: README with project overview, architecture, and setup instructions
- [x] **DEMO-04**: Architecture diagram showing all 8 agents and data flow

---

## v2 Requirements

### Analysis Enhancements

- [ ] Prompt Analyzer checks for ambiguous instructions
- [ ] Prompt Analyzer detects missing context in prompts
- [ ] Parallel execution of all 3 analyzers

### Diagnosis Enhancements

- [ ] Confidence scoring for diagnosis (0-100%)
- [ ] Multiple root cause candidates ranked by likelihood

### Validation

- [ ] Validation Loop re-runs failed scenario with fix applied
- [ ] Trace comparison shows before/after differences
- [ ] Automatic rollback if fix doesn't resolve failure

### Storage

- [ ] Fix history stored for RAG lookup
- [ ] Azure AI Search index over past fixes

---

## Out of Scope

- **Production deployment** — hackathon demo only, no hardening
- **Self-healing without approval** — fixes require human confirmation
- **Real-time dashboard** — focus on core diagnosis flow
- **Non-Foundry tracing** — tight Azure integration only
- **Code-level bug fixing** — agent debugging, not code repair
- **Copilot Agent Mode integration** — adds complexity without demo value

---

## Traceability

| REQ-ID | Phase | Status | Success Criteria |
|--------|-------|--------|------------------|
| FOUND-01 | Phase 1: Foundation | Complete | Foundry project accessible with tracing enabled |
| FOUND-02 | Phase 1: Foundation | Complete | BookingAgent reliably fails on DD/MM/YYYY dates |
| FOUND-03 | Phase 1: Foundation | Complete | SearchAgent reliably fails on ambiguous tool selection |
| FOUND-04 | Phase 1: Foundation | Complete | SummaryAgent reliably hallucinates on minimal sources |
| FOUND-05 | Phase 1: Foundation | Complete | Failure Detector catches all 3 failure types |
| FOUND-06 | Phase 1: Foundation | Approved (pending live Cosmos check) | Traces stored in Cosmos DB, retrievable by failure_id |
| ANLZ-01 | Phase 2: Analysis | Complete | Identifies failure step (N of M) for all test subjects |
| ANLZ-02 | Phase 2: Analysis | Complete | Extracts reasoning chain as structured list |
| ANLZ-03 | Phase 2: Analysis | Complete | Validates params against JSON schemas, reports mismatches |
| ANLZ-04 | Phase 2: Analysis | Complete | Detects wrong tool selection in SearchAgent scenario |
| ANLZ-05 | Phase 2: Analysis | Complete | Orchestrates analyzers and waits for completion |
| ANLZ-06 | Phase 2: Analysis | Complete | Produces unified FindingsReport with structured output |
| DIAG-01 | Phase 3: Diagnosis | Complete | Classifies into taxonomy (TOOL_MISUSE, HALLUCINATION, etc.) |
| DIAG-02 | Phase 3: Diagnosis | Complete | Produces root_cause with confidence score (0.0-1.0) |
| DIAG-03 | Phase 3: Diagnosis | Complete | Generates human-readable explanation |
| DIAG-04 | Phase 3: Diagnosis | Complete | Queries and links similar past failures |
| FIX-01 | Phase 3: Fixes | Complete | Produces PROMPT_FIX proposals for failures |
| FIX-02 | Phase 3: Fixes | Complete | Produces TOOL_CONFIG_FIX proposals for failures |
| FIX-03 | Phase 3: Fixes | Complete | Produces GUARDRAIL_FIX proposals for failures |
| FIX-04 | Phase 3: Fixes | Complete | Shows before/after diff for all proposed changes |
| DEMO-01 | Phase 4: Demo | Complete | Demo script written and rehearsed |
| DEMO-02 | Phase 4: Demo | Pending | 2-minute video recorded with voice-over *(manual recording/upload pending)* |
| DEMO-03 | Phase 4: Demo | Complete | README includes overview, architecture, setup, usage |
| DEMO-04 | Phase 4: Demo | Complete | Architecture diagram (PNG/SVG) shows all agents |

**Coverage:** 20/20 requirements mapped (100%)
