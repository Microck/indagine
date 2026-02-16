# Indagine

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

Indagine is a meta-agent system that helps debug other AI agents when they fail.

It captures a failure event, analyzes trace and tool behavior, diagnoses the root cause using a shared taxonomy, and proposes concrete fixes.

## Features

- Deterministic "subject" agents that fail predictably for repeatable debugging
- Trace + tool analyzers that produce structured findings
- Diagnosis engine with an explicit failure taxonomy
- Fix proposal generation with diffs for easy review
- Optional Azure integrations (Foundry, Cosmos) without making them mandatory

## Installation

Prereqs:
- Python 3.11+
- `uv`

```bash
uv sync
```

## Quick Start

Run the demo flow (mock mode):

```bash
uv run python demo/run_demo.py --mode mock
```

Run the test suite:

```bash
uv run pytest -q
```

## Usage

Run deterministic failure subjects:

```bash
uv run python -m src.subjects.run_subjects booking
uv run python -m src.subjects.run_subjects search
uv run python -m src.subjects.run_subjects summary
```

## Architecture

Artifacts:
- Diagram: `docs/architecture.png`
- Diagram source: `docs/architecture.mmd`
- Failure taxonomy: `docs/failure_taxonomy.md`

Agent roles shown in the diagram:
- BookingAgent
- SearchAgent
- SummaryAgent
- FailureDetector
- TraceAnalyzer
- ToolAnalyzer
- DiagnosisEngine
- FixGenerator

If you need to regenerate the PNG:

```bash
npx -y @mermaid-js/mermaid-cli -i docs/architecture.mmd -o docs/architecture.png
```

## Configuration

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

## Contributing

Issues and pull requests are welcome.

## License

Apache-2.0 (see `LICENSE`).
