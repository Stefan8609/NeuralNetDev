"""Task definitions for seismological machine learning."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class SeismologyTask(StrEnum):
    """Supported high-level learning tasks."""

    PHASE_PICKING = "phase_picking"
    EVENT_DETECTION = "event_detection"
    WAVEFORM_CLASSIFICATION = "waveform_classification"
    DENOISING = "denoising"
    MAGNITUDE_REGRESSION = "magnitude_regression"


class LabelKind(StrEnum):
    """How supervision is represented for a task."""

    POINT = "point"
    INTERVAL = "interval"
    CLASS = "class"
    CONTINUOUS = "continuous"
    SEQUENCE = "sequence"


@dataclass(frozen=True, slots=True)
class TaskSpec:
    """Describes a concrete modeling objective."""

    task: SeismologyTask
    label_kind: LabelKind
    prediction_target: str
    description: str


DEFAULT_TASK_SPECS: tuple[TaskSpec, ...] = (
    TaskSpec(
        task=SeismologyTask.PHASE_PICKING,
        label_kind=LabelKind.POINT,
        prediction_target="P or S arrival sample index",
        description="Predict the onset location of a seismic phase within a waveform window.",
    ),
    TaskSpec(
        task=SeismologyTask.EVENT_DETECTION,
        label_kind=LabelKind.INTERVAL,
        prediction_target="Event presence interval within a waveform window",
        description="Detect whether a time interval contains seismic event energy.",
    ),
    TaskSpec(
        task=SeismologyTask.WAVEFORM_CLASSIFICATION,
        label_kind=LabelKind.CLASS,
        prediction_target="Waveform class label",
        description="Assign a class such as earthquake, noise, quarry blast, or artifact.",
    ),
)
