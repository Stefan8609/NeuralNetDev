"""Task definitions for seismological machine learning."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class SeismologyTask(StrEnum):
    """Supported high-level learning tasks."""

    PHASE_PICKING = "phase_picking"
    DENOISING = "denoising"
    EVENT_DETECTION = "event_detection"
    EVENT_ASSOCIATION = "event_association"
    EARTHQUAKE_LOCATING = "earthquake_locating"
    TRAVEL_TIME_CONSISTENCY = "travel_time_consistency"
    MULTI_STATION_INTERPRETATION = "multi_station_interpretation"
    WAVEFORM_CLASSIFICATION = "waveform_classification"
    MAGNITUDE_REGRESSION = "magnitude_regression"


class LabelKind(StrEnum):
    """How supervision is represented for a task."""

    POINT = "point"
    INTERVAL = "interval"
    CLASS = "class"
    CONTINUOUS = "continuous"
    SEQUENCE = "sequence"


class StructureKind(StrEnum):
    """Primary structure presented to a model."""

    WAVEFORM = "waveform"
    STATION_GRAPH = "station_graph"
    EVENT_STATION_BIPARTITE = "event_station_bipartite"
    TEMPORAL_GRAPH = "temporal_graph"
    GEOMETRIC = "geometric"


@dataclass(frozen=True, slots=True)
class TaskSpec:
    """Describes a concrete modeling objective."""

    task: SeismologyTask
    label_kind: LabelKind
    structure_kind: StructureKind
    prediction_target: str
    description: str
    typical_nodes: tuple[str, ...]
    typical_edges: tuple[str, ...]
    typical_losses: tuple[str, ...]


DEFAULT_TASK_SPECS: tuple[TaskSpec, ...] = (
    TaskSpec(
        task=SeismologyTask.PHASE_PICKING,
        label_kind=LabelKind.POINT,
        structure_kind=StructureKind.WAVEFORM,
        prediction_target="P or S arrival sample index",
        description="Predict the onset location of a seismic phase within a waveform window.",
        typical_nodes=("waveform_window",),
        typical_edges=(),
        typical_losses=("cross_entropy", "gaussian_nll", "huber"),
    ),
    TaskSpec(
        task=SeismologyTask.DENOISING,
        label_kind=LabelKind.SEQUENCE,
        structure_kind=StructureKind.WAVEFORM,
        prediction_target="Clean waveform samples aligned to a noisy input window",
        description=(
            "Recover a cleaner waveform while preserving phase timing and amplitude structure."
        ),
        typical_nodes=("waveform_window",),
        typical_edges=(),
        typical_losses=("l1", "l2", "multi_resolution_stft"),
    ),
    TaskSpec(
        task=SeismologyTask.EVENT_DETECTION,
        label_kind=LabelKind.INTERVAL,
        structure_kind=StructureKind.WAVEFORM,
        prediction_target="Event presence interval within a waveform window",
        description="Detect whether a time interval contains seismic event energy.",
        typical_nodes=("waveform_window",),
        typical_edges=(),
        typical_losses=("binary_cross_entropy", "focal"),
    ),
    TaskSpec(
        task=SeismologyTask.EVENT_ASSOCIATION,
        label_kind=LabelKind.CLASS,
        structure_kind=StructureKind.EVENT_STATION_BIPARTITE,
        prediction_target="Assignment of picks to shared seismic events",
        description=(
            "Associate picks across stations into event hypotheses consistent with"
            " space-time geometry."
        ),
        typical_nodes=("pick", "station", "event_hypothesis"),
        typical_edges=("pick_to_station", "pick_to_event", "event_to_station"),
        typical_losses=("cross_entropy", "contrastive", "set_matching"),
    ),
    TaskSpec(
        task=SeismologyTask.EARTHQUAKE_LOCATING,
        label_kind=LabelKind.CONTINUOUS,
        structure_kind=StructureKind.GEOMETRIC,
        prediction_target="Event hypocenter and origin time",
        description=(
            "Infer source location from multi-station arrivals, geometry, and timing relations."
        ),
        typical_nodes=("pick", "station", "event_hypothesis"),
        typical_edges=("pick_to_station", "station_to_station", "event_to_station"),
        typical_losses=("l1", "huber", "gaussian_nll"),
    ),
    TaskSpec(
        task=SeismologyTask.TRAVEL_TIME_CONSISTENCY,
        label_kind=LabelKind.CONTINUOUS,
        structure_kind=StructureKind.GEOMETRIC,
        prediction_target="Residual between observed and physically plausible travel times",
        description=(
            "Model travel-time compatibility using station geometry, phase identity,"
            " and source hypotheses."
        ),
        typical_nodes=("pick", "station", "event_hypothesis"),
        typical_edges=("pick_to_station", "event_to_station", "travel_time_reference"),
        typical_losses=("l1", "huber", "gaussian_nll"),
    ),
    TaskSpec(
        task=SeismologyTask.MULTI_STATION_INTERPRETATION,
        label_kind=LabelKind.SEQUENCE,
        structure_kind=StructureKind.TEMPORAL_GRAPH,
        prediction_target="Structured interpretation over synchronized station windows",
        description=(
            "Interpret multi-station waveforms jointly through temporal and spatial connectivity."
        ),
        typical_nodes=("station_window", "pick"),
        typical_edges=("station_to_station", "temporal_context", "pick_to_station"),
        typical_losses=("cross_entropy", "binary_cross_entropy", "ctc"),
    ),
    TaskSpec(
        task=SeismologyTask.WAVEFORM_CLASSIFICATION,
        label_kind=LabelKind.CLASS,
        structure_kind=StructureKind.WAVEFORM,
        prediction_target="Waveform class label",
        description="Assign a class such as earthquake, noise, quarry blast, or artifact.",
        typical_nodes=("waveform_window",),
        typical_edges=(),
        typical_losses=("cross_entropy",),
    ),
    TaskSpec(
        task=SeismologyTask.MAGNITUDE_REGRESSION,
        label_kind=LabelKind.CONTINUOUS,
        structure_kind=StructureKind.GEOMETRIC,
        prediction_target="Event magnitude estimate from waveform and network context",
        description=(
            "Estimate magnitude using waveform amplitudes, source-station geometry,"
            " and network consistency."
        ),
        typical_nodes=("station_window", "station", "event_hypothesis"),
        typical_edges=("event_to_station", "station_to_station"),
        typical_losses=("l1", "huber", "gaussian_nll"),
    ),
)
