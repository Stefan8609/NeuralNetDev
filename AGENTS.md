# Agent Guide

## Mission

This repository is for building maintainable seismology ML tooling that can grow from
simple waveform baselines to graph neural networks and geometric deep learning methods.
The current stage is architecture-first: keep the codebase easy to navigate, reproducible,
scientifically explicit, and ready for domain-specific implementation.

## Primary objectives

1. Build a maintainable Python package for seismic ML workflows.
2. Keep data handling, model definition, training, and evaluation separated.
3. Support waveform, graph, and geometry-aware representations without premature framework lock-in.
4. Prefer small, typed modules over notebook-only logic.
5. Treat reproducibility and traceability as first-class requirements.

## Navigation

- Start with [MANIFEST.md](./MANIFEST.md) for the repository map.
- Use [README.md](./README.md) for onboarding and commands.
- Use [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md) for the target system design.
- Use [docs/ROADMAP.md](./docs/ROADMAP.md) for milestone sequencing.
- Use [configs/MANIFEST.md](./configs/MANIFEST.md) before adding experiment configs.
- Use [src/seismo_nn/MANIFEST.md](./src/seismo_nn/MANIFEST.md) before editing package code.

## Working conventions

- Keep domain concepts explicit: waveform windows, picks, events, stations, channels, labels, graphs, coordinates, and uncertainties.
- Add dependencies only when a concrete workflow requires them.
- Prefer library code in `src/` and use notebooks only for exploration.
- Preserve clean interfaces so future backends can use NumPy, PyTorch, or other frameworks.
- When proposing a method, state the nodes, edges, features, targets, losses, and the seismological structure being exploited.
- Start with the simplest correct baseline before suggesting deeper message passing, heterogeneous graphs, or equivariant models.

## Near-term implementation priorities

1. Define dataset, station, pick, and graph schemas with explicit semantics.
2. Add baseline task pipelines for phase picking, event detection, and denoising.
3. Add graph-ready formulations for multi-station interpretation and event association.
4. Add train/eval entrypoints once model dependencies are selected.
5. Expand tests from smoke coverage to behavior and invariants.
