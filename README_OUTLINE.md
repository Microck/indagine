# README Outline: indagine

Generated from:
- `README.md` headings (verbatim)
- Project signals: `pyproject.toml`, `uv.lock`, `.env.example`, `docs/`

## 1) Current README headings (verbatim)

1. # Indagine
2. ## API / CLI reference
3. ## Support / Community
4. ## Security
5. ## Changelog / Releases
6. ## Roadmap
7. ## What you get
8. ## Demo (2 minutes)
9. ## Installation
10. ## Quick start
11. ## How it works
12. ## Project layout
13. ## Configuration (optional)
14. ## Verification
15. ## Development
16. ## Contributing
17. ## License

## 2) Recommended outline (top-starred repo pattern, specialized for this project)

1. # Indagine
2. Intro: one-line value proposition
3. (Optional) Badges
4. ## What you get
5. ## Quickstart
6. ## Installation
7. ## Usage
8. ## Configuration
9. ## Verification (tests / checks)
10. ## How it works
11. ## Architecture
12. ## Project layout
13. ## API / CLI reference
14. ## Development
15. ## Testing
16. ## Contributing
17. ## Support / Community
18. ## Security
19. ## License
20. ## Changelog / Releases
21. (Optional) ## Roadmap

## 3) Mapping: current -> recommended

| Current heading | Recommended section |
| --- | --- |
| # Indagine | Title + intro + (optional) badges |
| ## API / CLI reference | API / CLI reference |
| ## Support / Community | Support / Community |
| ## Security | Security |
| ## Changelog / Releases | Changelog / Releases |
| ## Roadmap | Roadmap |
| ## What you get | What you get |
| ## Demo (2 minutes) | Quickstart / Usage |
| ## Installation | Installation |
| ## Quick start | Quickstart / Usage / Testing |
| ## How it works | How it works / Architecture |
| ## Project layout | Project layout |
| ## Configuration (optional) | Configuration |
| ## Verification | Verification / Testing |
| ## Development | Development |
| ## Contributing | Contributing |
| ## License | License |

## 4) Missing sections checklist (content to fill; headings now exist in `README.md`)

- [ ] API / CLI reference (add arguments/examples for each entry point)
- [ ] Support / Community (add where to ask questions: issues/discussions/contact)
- [ ] Security (add security reporting process; consider adding `SECURITY.md`)
- [ ] Changelog / Releases (add link to tags/releases; consider adding `CHANGELOG.md`)
- [ ] Roadmap (decide if `TODO.md` is the canonical source)

## 5) Ready-to-copy README skeleton (succinct, non-destructive)

````md
# Indagine

Indagine is a meta-agent system for debugging other AI agents when they fail.

<!-- Optional: badges (license, build, python version) -->

<!-- top-readme: begin -->
## API / CLI reference

- [demo/run_demo.py](demo/run_demo.py)
- [src/subjects/run_subjects.py](src/subjects/run_subjects.py)
- [src/scripts/verify_foundry.py](src/scripts/verify_foundry.py)
- [src/scripts/run_and_capture.py](src/scripts/run_and_capture.py)

## Support / Community

- [docs/](docs/)

## Security

## Changelog / Releases

- [pyproject.toml](pyproject.toml)

## Roadmap

- [TODO.md](TODO.md)
<!-- top-readme: end -->

## What you get

- TODO: 4-6 bullets describing outcomes/features

## Quickstart

Prereqs:
- Python 3.11+
- `uv`

```bash
uv sync
uv run python demo/run_demo.py --mode mock
````

## Installation

```bash
uv sync
```

## Usage

Run a deterministic failure subject:

```bash
uv run python -m src.subjects.run_subjects booking
```

Run the demo end-to-end:

```bash
uv run python demo/run_demo.py --mode live --subject booking --store memory
```

## Configuration (optional)

Create `.env` from `.env.example` when enabling Azure/Foundry verification:

```bash
cp .env.example .env
```

TODO: document the minimum env vars for each optional integration.

## Verification

```bash
uv run pytest -q
```

Optional (Foundry reachability):

```bash
uv run python -m src.scripts.verify_foundry --strict
```

Optional (Cosmos trace capture roundtrip):

```bash
uv run python -m src.scripts.run_and_capture --store cosmos
```

## How it works

TODO: 5-step pipeline overview.

Key artifacts:
- `docs/failure_taxonomy.md`
- `docs/architecture.mmd`

## Project layout

- `src/subjects/` deterministic agents that fail in known ways
- `src/analyzers/` trace + tool analyzers that emit structured findings
- `src/core/` pipeline orchestration, diagnosis, fix generation, tracing
- `src/storage/` in-memory and Cosmos backends
- `demo/` demo script + fixture output
- `docs/` architecture diagram + failure taxonomy

## API / CLI reference

- `demo/run_demo.py` (modes, subjects, stores)
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

TODO: contribution guidelines (or add `CONTRIBUTING.md`).

## Support / Community

TODO: where to ask questions (issues/discussions/contact).

## Security

TODO: security reporting process (or add `SECURITY.md`).

## License

Apache-2.0 (see `LICENSE`).

## Changelog / Releases

TODO: link to Git tags / GitHub Releases; describe versioning.

## Roadmap (optional)

TODO: link to `TODO.md` or milestones.
```
