# Package Manifest

## Purpose

This package contains reusable building blocks for seismological machine learning.
The current design favors typed interfaces and clear boundaries over early framework
lock-in, with explicit room for waveform, graph, and geometric modeling.

## Files

- `__init__.py`: package exports and version.
- `config.py`: repository path helpers and shared constants.
- `tasks.py`: task and label definitions.
- `pipeline.py`: waveform, station, pick, and graph example schemas.
- `models.py`: model interface and configuration contracts.
- `training.py`: training configuration and run summaries.
- `evaluation.py`: evaluation summaries and metric records.
- `seisbench.py`: lightweight helpers for SeisBench exploration and schema bridging.

## How to extend

- Add new domain enums or task-level schemas in `tasks.py`.
- Add waveform, station, pick, or graph record structures in `pipeline.py`.
- Add abstract or lightweight model interfaces in `models.py`.
- Keep heavyweight framework code in new subpackages once dependencies are added.

## Guardrails

- Do not hide assumptions about waveform shapes in random helper functions.
- Do not hide assumptions about graph connectivity or geometry in random helper functions.
- Keep metadata available alongside arrays whenever possible.
- Avoid coupling evaluation logic directly to one trainer implementation.
