# Indagine - Test & Smoke Checklist

Goal: run the exact checks needed before recording the submission video and submitting.

## 0) Repo sanity

```bash
cd projects/indagine
git status --porcelain
```

Expected: no output.

## 1) Install deps (uv)

```bash
cd projects/indagine
uv sync --frozen
```

## 2) Automated tests

```bash
cd projects/indagine
uv run pytest -q
```

## 3) Demo smoke (judge-safe)

```bash
cd projects/indagine
uv run python demo/run_demo.py --mode mock
```

Expected: end-to-end output including failure detection, findings, diagnosis, and at least one fix diff.

## 4) Optional: Foundry strict smoke

This fails fast if the required Foundry env vars aren’t set.

```bash
cd projects/indagine
uv run python -m src.scripts.verify_foundry --strict
```

## 5) Optional: Cosmos trace-store roundtrip

```bash
cd projects/indagine

export COSMOS_ENDPOINT=...
export COSMOS_KEY=...
export COSMOS_DATABASE=...
export COSMOS_CONTAINER_TRACES=...

uv run python -m src.scripts.run_and_capture --store cosmos
```

## 6) Submission artifacts

- README: `README.md`
- Architecture diagram: `docs/architecture.png` (source: `docs/architecture.mmd`)
- Demo runner: `demo/run_demo.py`
- Mock fixture: `demo/sample_output.md`
- Voiceover script: `demo/voiceover.md`
- Optional local video artifact: `demo/video.mp4`
