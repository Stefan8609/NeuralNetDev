# Configs Manifest

## Purpose

The `configs/` directory stores experiment-facing configuration files for reproducible
research runs.

## What belongs here

- dataset source and split settings
- waveform window and preprocessing settings
- task-specific targets and losses
- model family selection
- train/eval runtime settings

## Guardrails

- Keep configs small, explicit, and reviewable.
- Prefer one config per experiment family or task milestone.
- Do not hide scientific assumptions like coordinate frames or travel-time provenance.
