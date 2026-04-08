"""Model contracts for seismological tasks."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Protocol

import numpy as np
from numpy.typing import NDArray

from seismo_nn.tasks import SeismologyTask, StructureKind

ModelInput = NDArray[np.float64]
ModelOutput = NDArray[np.float64]


class ModelFamily(StrEnum):
    """High-level modeling families supported by the scaffold."""

    WAVEFORM = "waveform"
    GRAPH = "graph"
    GEOMETRIC = "geometric"


@dataclass(frozen=True, slots=True)
class ModelSpec:
    """Framework-agnostic description of a model family."""

    name: str
    task: SeismologyTask
    family: ModelFamily
    structure_kind: StructureKind
    input_channels: int
    input_samples: int | None
    output_description: str
    node_features: tuple[str, ...] = ()
    edge_features: tuple[str, ...] = ()
    target_names: tuple[str, ...] = ()
    loss_names: tuple[str, ...] = ()
    geometry_aware: bool = False
    equivariant: bool = False
    hyperparameters: dict[str, int | float | str | bool] = field(default_factory=dict)


class SeismologyModel(Protocol):
    """Minimal model interface for future implementations."""

    spec: ModelSpec

    def predict(self, inputs: ModelInput) -> ModelOutput:
        """Return model outputs for a batch of waveform windows."""
