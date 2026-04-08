# Agent Guide

## Mission

This repository is for building neural-network-based tooling for seismological tasks.
The current stage is architecture-first: keep the codebase easy to navigate, reproducible,
and ready for domain-specific implementation.

## Primary objectives

1. Build a maintainable Python package for seismic ML workflows.
2. Keep data handling, model definition, training, and evaluation separated.
3. Prefer small, typed modules over notebook-only logic.
4. Treat reproducibility and traceability as first-class requirements.

## Navigation

- Start with [MANIFEST.md](./MANIFEST.md) for the repository map.
- Use [README.md](./README.md) for onboarding and commands.
- Use [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md) for the target system design.
- Use [docs/ROADMAP.md](./docs/ROADMAP.md) for milestone sequencing.
- Use [src/seismo_nn/MANIFEST.md](./src/seismo_nn/MANIFEST.md) before editing package code.

## Working conventions

- Keep domain concepts explicit: waveform windows, picks, events, stations, channels, labels.
- Add dependencies only when a concrete workflow requires them.
- Prefer library code in `src/` and use notebooks only for exploration.
- Preserve clean interfaces so future backends can use NumPy, PyTorch, or other frameworks.

## Near-term implementation priorities

1. Define dataset schemas and window extraction rules.
2. Add baseline task pipelines for phase picking and event detection.
3. Add train/eval entrypoints once model dependencies are selected.
4. Expand tests from smoke coverage to behavior and invariants.
