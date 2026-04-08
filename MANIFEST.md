# Repository Manifest

## Purpose

`seismo-nn` is a scaffold for machine-learning systems that operate on seismological
waveform, graph-structured, and geometry-aware data. The repository is organized so an
engineer or coding agent can quickly locate data interfaces, model abstractions, training
logic, configuration, and project guidance.

## Fast orientation

- `README.md`: project overview, environment setup, and common commands.
- `AGENTS.md`: contributor guidance for Codex and other agents.
- `docs/`: architecture, roadmap, and development policy.
- `notebooks/`: exploratory analysis notebooks that should stay thin and reproducible.
- `configs/`: experiment and workflow configuration files.
- `src/seismo_nn/`: package source for reusable library code.
- `tests/`: validation and regression coverage.
- `scripts/`: bootstrap and automation helpers.

## Current maturity

This repository is in the scaffold-and-architecture phase.
What exists now:
- packaging and developer tooling
- project configuration
- domain-aware module boundaries
- planning documents for waveform, graph, and geometric seismic ML work

What is intentionally still lightweight:
- dataset ingestion
- concrete model implementations
- train/eval entrypoints
- graph construction utilities
- exploratory notebooks for data familiarization

## Target problem areas

The codebase is intended to support one or more of these tasks:
- phase picking
- denoising
- event detection
- event association
- earthquake locating
- travel-time consistency modeling
- multi-station waveform interpretation
- waveform classification
- magnitude or quality regression

## Recommended edit paths

- New domain abstractions: `src/seismo_nn/tasks.py`
- Data/window/graph schemas: `src/seismo_nn/pipeline.py`
- Model contracts: `src/seismo_nn/models.py`
- Training contracts: `src/seismo_nn/training.py`
- Evaluation contracts: `src/seismo_nn/evaluation.py`
- Project planning docs: `docs/`
- Experiment configs: `configs/`

## Conventions

- Keep core interfaces framework-light until a model stack is chosen.
- Use typed dataclasses and enums to make intent obvious.
- Keep orchestration separate from numerical implementation details.
- Avoid hidden assumptions about sample rate, channel order, graph connectivity, or label semantics.
