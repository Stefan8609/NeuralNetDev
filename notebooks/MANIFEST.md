# Notebooks Manifest

## Purpose

Notebooks are for exploration, inspection, and data familiarization.
If logic becomes reusable or scientifically important, move it into `src/`.

## Files

- `seisbench_demo.ipynb`: first-touch walkthrough for listing datasets, loading one sample dataset, plotting traces, and bridging into `WaveformWindow`.

## Guardrails

- Keep notebooks runnable from a fresh repo checkout.
- Prefer importing helpers from `src/` over pasting large code cells.
- Keep cache and data paths explicit so downloads do not silently spill into home directories.
