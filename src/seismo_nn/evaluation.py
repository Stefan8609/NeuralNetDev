"""Evaluation records for seismic ML experiments."""

from __future__ import annotations

from dataclasses import dataclass

from seismo_nn.tasks import SeismologyTask


@dataclass(frozen=True, slots=True)
class MetricRecord:
    """A single metric value with optional units."""

    name: str
    value: float
    units: str | None = None
    uncertainty: float | None = None


@dataclass(frozen=True, slots=True)
class EvaluationSummary:
    """Collection of metrics for one task on one dataset split."""

    task: SeismologyTask
    dataset_split: str
    metrics: tuple[MetricRecord, ...]
    notes: str = ""
