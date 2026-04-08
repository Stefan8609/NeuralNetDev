# Roadmap

## Milestone 1: Navigation and architecture

- establish repository manifests
- define package boundaries
- document the first seismology tasks

## Milestone 2: Data contracts

- add waveform window schemas
- define metadata and label records
- choose one dataset family or ingestion adapter

## Milestone 3: Baseline task

- select one concrete task:
  phase picking, event detection, or classification
- implement a baseline dataset builder
- add a simple model contract and dummy baseline

## Milestone 4: Training loop

- choose framework, likely PyTorch
- add optimizer, loss, checkpoint, and metrics plumbing
- store reproducible run configuration

## Milestone 5: Evaluation and iteration

- benchmark on held-out data
- compare alternative architectures
- document failure modes and data issues

## Recommended first task

Phase picking is the best first target when labeled picks are available.
If labels are weak or sparse, event detection is often the more practical entry point.
