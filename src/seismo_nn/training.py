"""Training configuration contracts."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

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
    config_name: str = "baseline"
    output_dir: str = "artifacts"
    notes: str = ""

    def __post_init__(self) -> None:
        split_sum = self.train_split + self.validation_split + self.test_split
        if self.batch_size <= 0:
            msg = "batch_size must be positive"
            raise ValueError(msg)
        if self.epochs <= 0:
            msg = "epochs must be positive"
            raise ValueError(msg)
        if self.learning_rate <= 0:
            msg = "learning_rate must be positive"
            raise ValueError(msg)
        if not np.isclose(split_sum, 1.0):
            msg = "train/validation/test splits must sum to 1.0"
            raise ValueError(msg)


@dataclass(frozen=True, slots=True)
class TrainingRunSummary:
    """Minimal metadata to describe a completed or planned run."""

    run_name: str
    config: TrainingConfig
    dataset_name: str
    artifact_paths: tuple[str, ...] = ()
    tags: tuple[str, ...] = ()
    metadata: dict[str, str | float | int] = field(default_factory=dict)
