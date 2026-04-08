# Package Manifest

## Purpose

This package contains reusable building blocks for seismological machine learning.
The current design favors typed interfaces and clear boundaries over early framework lock-in.

## Files

- `__init__.py`: package exports and version.
- `config.py`: repository path helpers and shared constants.
- `tasks.py`: task and label definitions.
- `pipeline.py`: waveform window and preprocessing schemas.
- `models.py`: model interface and configuration contracts.
- `training.py`: training configuration and run summaries.
- `evaluation.py`: evaluation summaries and metric records.

## How to extend

- Add new domain enums or task-level schemas in `tasks.py`.
- Add data record structures in `pipeline.py`.
- Add abstract or lightweight model interfaces in `models.py`.
- Keep heavyweight framework code in new subpackages once dependencies are added.

## Guardrails

- Do not hide assumptions about waveform shapes in random helper functions.
- Keep metadata available alongside arrays whenever possible.
- Avoid coupling evaluation logic directly to one trainer implementation.
