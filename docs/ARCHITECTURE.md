# Architecture

## Goal

Build a seismology-focused neural network toolkit that can move from raw waveform access
to trainable datasets, baseline models, graph/geometric representations, and reproducible
evaluation.

## Core flow

1. Load waveform and metadata from a chosen data source.
2. Convert records into normalized time windows with explicit labels.
3. Build task-specific examples as waveform windows, station graphs, or event-station graphs.
4. Route examples into a task-specific model interface.
5. Train against a declared objective with tracked hyperparameters and config provenance.
6. Evaluate on task-level metrics and preserve experiment metadata.

## Modeling layers

### Waveform models

Use for the simplest correct baseline when a task can be solved from fixed windows.
These models primarily exploit local waveform morphology and onset shape.

### Graph models

Use when the task depends on relations between stations, picks, or event hypotheses.
These models exploit cross-station structure, association logic, and temporal connectivity.

### Geometric or equivariant models

Use when source-receiver geometry should shape the inductive bias.
These models exploit coordinates, travel-time relations, and physically meaningful invariances.

## Package boundaries

### `tasks.py`

Defines the task taxonomy and label semantics for seismic ML problems.
This should answer: what are we predicting, over what structure, and in what form?

### `pipeline.py`

Defines data-facing schemas for waveform windows, stations, picks, graph examples, and
preprocessing configuration. Raw IO adapters can depend on external packages later, but
the shared types should stay stable here.

### `seisbench.py`

Defines lightweight exploration helpers for SeisBench so notebook setup, local cache
paths, and schema bridging stay explicit and reusable without turning notebooks into
core infrastructure.

### `models.py`

Defines model interfaces and configuration objects across waveform, graph, and geometric
families. Concrete implementations can later wrap PyTorch or another framework without
changing the rest of the repository contract.

### `training.py`

Defines training configuration and run metadata. This is where reproducibility knobs
and experiment identity should live even before a full trainer exists.

### `evaluation.py`

Defines evaluation outputs and task-specific metrics. This keeps quality criteria visible
and prevents metrics from being scattered across ad hoc scripts.

## Configs

Store experiment-facing configuration files in `configs/`.
Keep config files small and task-oriented so scientific assumptions remain reviewable.

## Suggested future subpackages

Once implementation becomes more concrete, grow into this shape:

```text
src/seismo_nn/
├── data/
├── models/
├── training/
├── evaluation/
├── tasks.py
└── config.py
```

## Domain assumptions to keep explicit

- waveform sample rate
- window length and stride
- component ordering, such as `Z`, `N`, `E`
- station and event metadata provenance
- station coordinates and coordinate reference choice
- graph node and edge semantics
- travel-time assumptions and velocity-model provenance
- label uncertainty and noisy annotations
- train/validation/test split policy

## First production-grade baselines

Start with the simplest correct baseline before adding GNN or equivariant complexity.

Recommended order:
1. waveform baseline for phase picking or event detection
2. graph-ready data example for multi-station context
3. simple station-graph or association baseline
4. geometry-aware locating or travel-time consistency model

Each method should state:
- nodes
- edges
- features
- targets
- losses
- physical constraints or uncertainties

The first waveform baselines still exercise the core path:
- waveform ingestion
- window extraction
- label alignment
- model forward pass
- thresholded or regression-style evaluation
