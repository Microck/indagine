# Indagine

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

Indagine is a meta-agent system for debugging other AI agents when they fail.

It analyzes trace + tool behavior, classifies the root cause using a shared taxonomy, and proposes concrete fixes (diff-first).

## Quickstart

Prereqs:
- Python 3.11+
- `uv`

```bash
uv sync
uv run python demo/run_demo.py --mode mock
```

## Installation

```bash
uv sync
```

## Usage

Run a deterministic failure subject:

```bash
uv run python -m src.subjects.run_subjects booking
```

Run the end-to-end demo:

```bash
uv run python demo/run_demo.py --mode live --subject booking --store memory
```

## Configuration

Optional integrations use environment variables.

Create `.env` from `.env.example` if enabling Azure/Foundry verification:

```bash
cp .env.example .env
```

TODO: document the minimum env vars for each optional integration.

## How it works

TODO: add a 5-step pipeline overview.

Key artifacts:
- `docs/failure_taxonomy.md`
- `docs/architecture.mmd`

## Project layout

- `src/subjects/` deterministic agents that fail in known ways
- `src/analyzers/` trace + tool analyzers that emit structured findings
- `src/core/` pipeline orchestration, diagnosis, fix generation, tracing
- `src/storage/` in-memory and Cosmos backends
- `demo/` demo runner + fixture output
- `docs/` architecture diagram + failure taxonomy

## API / CLI reference

- `demo/run_demo.py`
- `python -m src.subjects.run_subjects <subject>`
- `python -m src.scripts.verify_foundry`
- `python -m src.scripts.run_and_capture`

TODO: add arguments/examples for each.

## Development

Lint:

```bash
uv run ruff check .
```

## Testing

```bash
uv run pytest -q
```

## Contributing

Issues and pull requests are welcome.

## Support / Community

TODO: add where to ask questions (Issues / Discussions) and what to include in a bug report.

## Security

TODO: add a security reporting process (or add `SECURITY.md` and link it).

## License

Apache-2.0 (see `LICENSE`).

## Changelog / Releases

TODO: link to GitHub Releases or add `CHANGELOG.md`.

## Roadmap

- `TODO.md`
