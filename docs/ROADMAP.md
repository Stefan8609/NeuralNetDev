# Roadmap

## Milestone 1: Navigation and architecture

- establish repository manifests
- define package boundaries
- document waveform, graph, and geometric seismology tasks

## Milestone 2: Data contracts

- add waveform window schemas
- define station, pick, and graph metadata records
- choose one dataset family or ingestion adapter
- create `configs/` conventions for reproducible experiments

## Milestone 3: Baseline task

- select one concrete task:
  phase picking, event detection, or denoising
- implement a baseline dataset builder
- add a simple model contract and dummy baseline
- document the matching multi-station formulation if the task benefits from network context

## Milestone 4: Multi-station graph baseline

- define nodes, edges, features, targets, and losses for one graph task
- start with the simplest useful graph, likely a station graph or pick-event graph
- keep the implementation interpretable before optimizing architecture depth

## Milestone 5: Training loop and evaluation

- choose framework, likely PyTorch
- add optimizer, loss, checkpoint, and metrics plumbing
- store reproducible run configuration
- benchmark on held-out data
- compare alternative architectures
- document failure modes and data issues

## Milestone 6: Geometric and physically informed models

- add coordinate-aware models for locating or travel-time residual prediction
- test uncertainty-aware and physically meaningful losses
- explore equivariant models only after simpler baselines are trustworthy

## Recommended first task

Phase picking is the best first target when labeled picks are available.
If labels are weak or sparse, event detection is often the more practical entry point.
