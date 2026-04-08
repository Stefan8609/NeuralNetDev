# SeisBench Playground

## Why start with a notebook

Yes, notebooking is a reasonable first step for SeisBench in this repository.
It is the fastest way to:

- inspect dataset metadata columns
- look at a few raw waveform examples
- confirm sampling rates, channel order, and pick fields
- test simple filters before deciding what reusable pipeline code belongs in `src/`

That said, keep notebooks thin.
Once a step becomes repeatable or scientifically important, move it into package code.

## Recommended first steps

1. Open the demo notebook at `notebooks/seisbench_demo.ipynb`.
2. Start with `DummyDataset` to learn the API on a small dataset.
3. Inspect `dataset.metadata.head()` and identify the fields you care about.
4. Pull one sample with `dataset.get_sample(idx)`.
5. Convert it into `WaveformWindow` so the repository's schema stays explicit.
6. Only after that, decide which concrete benchmark dataset to adopt for a baseline task.

## Launch

Create the environment and start Jupyter:

```bash
uv sync
make notebook
```

The helper utilities in `src/seismo_nn/seisbench.py` automatically redirect SeisBench and
Matplotlib caches into the repository:

- `.seisbench-cache/`
- `.mplconfig/`
- `.cache/`

This keeps exploratory runs more reproducible and avoids hidden writes into your home directory.

## Suggested progression

- `DummyDataset`: smallest first-touch option for learning the API
- `ETHZ` or `GEOFON`: useful next stops for regional/event-style exploration
- `STEAD`: strong benchmark option once you know which task and metadata fields you need

## What belongs in notebooks vs `src/`

Keep in notebooks:

- ad hoc metadata inspection
- one-off plots
- hypothesis generation
- small slices of exploratory filtering

Move to `src/`:

- cache/path setup
- schema conversion
- dataset selection logic
- train/eval preprocessing
- anything you expect to rerun or test
