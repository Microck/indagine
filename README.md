# Indagine

Indagine is a meta-agent system that debugs other AI agents when they fail: it captures a failure event, analyzes trace and tool behavior, diagnoses root cause with a shared taxonomy, and proposes concrete fixes.

Built for: Microsoft AI Dev Days Hackathon 2026
Categories: AI Apps and Agents, Best Use of Foundry, Best Multi-Agent System
Demo video: <paste hosted link>

## Quickstart (Judge-safe)

These commands run without Azure credentials (deterministic subjects + mock demo path).

```bash
uv sync
uv run pytest -q
uv run python demo/run_demo.py --mode mock
```

## What It Does

End-to-end flow:

```text
subject failure -> failure detection -> trace/tool analysis -> diagnosis -> fix diff
```

Run the deterministic failure subjects:

```bash
uv run python -m src.subjects.run_subjects booking
uv run python -m src.subjects.run_subjects search
uv run python -m src.subjects.run_subjects summary
```

## Architecture

Diagram: `docs/architecture.png`
Diagram source: `docs/architecture.mmd`
Failure taxonomy: `docs/failure_taxonomy.md`

Agent definition for DEMO-04:
- BookingAgent
- SearchAgent
- SummaryAgent
- FailureDetector
- TraceAnalyzer
- ToolAnalyzer
- DiagnosisEngine
- FixGenerator

IndagineController and IndaginePipeline are orchestration glue (shown in the diagram), not counted as separate agents.

If you need to regenerate the PNG:

```bash
npx -y @mermaid-js/mermaid-cli -i docs/architecture.mmd -o docs/architecture.png
```

## Configuration (Optional Live Integrations)

Create `.env` from `.env.example`.

Foundry (optional live verification):
- `FOUNDRY_PROJECT_ENDPOINT`
- `FOUNDRY_MODEL_DEPLOYMENT`
- `APPLICATIONINSIGHTS_CONNECTION_STRING` (optional)

Cosmos backends (optional):
- `COSMOS_ENDPOINT`
- `COSMOS_KEY`
- `COSMOS_DATABASE`
- `COSMOS_CONTAINER_TRACES`
- `COSMOS_CONTAINER_FIXES`

## Verification

Automated:

```bash
uv run pytest -q
```

Optional (live Foundry reachability):

```bash
uv run python -m src.scripts.verify_foundry --strict
```

Optional (Cosmos trace capture roundtrip):

```bash
uv run python -m src.scripts.run_and_capture --store cosmos
```

## Demo Assets

- Scenario script: `demo/scenario.md`
- Recording checklist: `demo/recording_checklist.md`
- Submission checklist: `demo/submission_checklist.md`

## License

Apache-2.0 (see `LICENSE`).
