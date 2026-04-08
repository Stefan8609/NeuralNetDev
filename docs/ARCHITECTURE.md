# Architecture

## Goal

Build a seismology-focused neural network toolkit that can move from raw waveform access
to trainable datasets, baseline models, and reproducible evaluation.

## Core flow

1. Load waveform and metadata from a chosen data source.
2. Convert records into normalized time windows with explicit labels.
3. Route windows into a task-specific model interface.
4. Train against a declared objective with tracked hyperparameters.
5. Evaluate on task-level metrics and preserve experiment metadata.

## Package boundaries

### `tasks.py`

Defines the task taxonomy and label semantics for seismic ML problems.
This should answer: what are we predicting, over what window, and in what form?

### `pipeline.py`

Defines data-facing schemas for waveform windows, dataset examples, and preprocessing
configuration. Raw IO adapters can depend on external packages later, but the shared
types should stay stable here.

### `models.py`

Defines model interfaces and configuration objects. Concrete implementations can later
wrap PyTorch or another framework without changing the rest of the repository contract.

### `training.py`

Defines training configuration and run metadata. This is where reproducibility knobs
should live even before a full trainer exists.

### `evaluation.py`

Defines evaluation outputs and task-specific metrics. This keeps quality criteria visible
and prevents metrics from being scattered across ad hoc scripts.

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
- label uncertainty and noisy annotations
- train/validation/test split policy

## First production-grade baseline

The strongest first baseline is usually phase picking or event detection on fixed windows.
Both tasks exercise the same critical path:
- waveform ingestion
- window extraction
- label alignment
- model forward pass
- thresholded or regression-style evaluation
