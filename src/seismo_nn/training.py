"""Training configuration contracts."""

from __future__ import annotations

from dataclasses import dataclass, field

from seismo_nn.tasks import SeismologyTask


@dataclass(frozen=True, slots=True)
class TrainingConfig:
    """Reproducible training settings shared across implementations."""

    task: SeismologyTask
    batch_size: int = 32
    epochs: int = 20
    learning_rate: float = 1e-3
    seed: int = 0
    train_split: float = 0.7
    validation_split: float = 0.15
    test_split: float = 0.15
    notes: str = ""


@dataclass(frozen=True, slots=True)
class TrainingRunSummary:
    """Minimal metadata to describe a completed or planned run."""

    run_name: str
    config: TrainingConfig
    dataset_name: str
    artifact_paths: tuple[str, ...] = ()
    tags: tuple[str, ...] = ()
    metadata: dict[str, str | float | int] = field(default_factory=dict)
