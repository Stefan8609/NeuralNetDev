"""Model contracts for seismological tasks."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

import numpy as np
from numpy.typing import NDArray

from seismo_nn.tasks import SeismologyTask

ModelInput = NDArray[np.float64]
ModelOutput = NDArray[np.float64]


@dataclass(frozen=True, slots=True)
class ModelSpec:
    """Framework-agnostic description of a model family."""

    name: str
    task: SeismologyTask
    input_channels: int
    input_samples: int
    output_description: str
    hyperparameters: dict[str, int | float | str | bool] = field(default_factory=dict)


class SeismologyModel(Protocol):
    """Minimal model interface for future implementations."""

    spec: ModelSpec

    def predict(self, inputs: ModelInput) -> ModelOutput:
        """Return model outputs for a batch of waveform windows."""
