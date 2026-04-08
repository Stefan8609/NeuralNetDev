"""Data-facing schemas for waveform, graph, and geometric seismic ML pipelines."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

import numpy as np
from numpy.typing import NDArray

from seismo_nn.tasks import SeismologyTask

WaveformArray = NDArray[np.float64]
Coordinate3D = tuple[float, float, float]
MetadataValue = str | float | int | bool


@dataclass(frozen=True, slots=True)
class WindowSpec:
    """Defines how waveform windows are constructed."""

    sample_rate_hz: float
    duration_seconds: float
    stride_seconds: float
    channels: tuple[str, ...] = ("Z", "N", "E")

    def __post_init__(self) -> None:
        if self.sample_rate_hz <= 0:
            msg = "sample_rate_hz must be positive"
            raise ValueError(msg)
        if self.duration_seconds <= 0:
            msg = "duration_seconds must be positive"
            raise ValueError(msg)
        if self.stride_seconds <= 0:
            msg = "stride_seconds must be positive"
            raise ValueError(msg)
        if not self.channels:
            msg = "channels must not be empty"
            raise ValueError(msg)


@dataclass(frozen=True, slots=True)
class WaveformWindow:
    """A fixed-size waveform segment and its metadata."""

    task: SeismologyTask
    samples: WaveformArray
    sample_rate_hz: float
    station_code: str
    event_id: str | None = None
    channel_order: tuple[str, ...] = ("Z", "N", "E")
    metadata: dict[str, MetadataValue] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.samples.ndim != 2:
            msg = "samples must have shape (channels, samples)"
            raise ValueError(msg)
        if self.samples.shape[0] != len(self.channel_order):
            msg = "channel_order length must match the first samples dimension"
            raise ValueError(msg)
        if self.sample_rate_hz <= 0:
            msg = "sample_rate_hz must be positive"
            raise ValueError(msg)


@dataclass(frozen=True, slots=True)
class NormalizationSpec:
    """Preprocessing configuration applied before model input."""

    demean: bool = True
    detrend: bool = False
    peak_normalize: bool = True
    clip_value: float | None = None


@dataclass(frozen=True, slots=True)
class Station:
    """Static metadata for a seismic station."""

    code: str
    network: str
    coordinates: Coordinate3D
    elevation_m: float | None = None
    metadata: dict[str, MetadataValue] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class PickObservation:
    """Observed or predicted phase arrival at one station."""

    station_code: str
    phase_label: str
    arrival_time_seconds: float
    probability: float | None = None
    uncertainty_seconds: float | None = None
    metadata: dict[str, MetadataValue] = field(default_factory=dict)


class GraphNodeType(StrEnum):
    """Supported node roles for graph-structured seismic data."""

    STATION = "station"
    PICK = "pick"
    EVENT = "event"
    WINDOW = "window"


class GraphEdgeType(StrEnum):
    """Supported edge semantics for graph-structured seismic data."""

    STATION_TO_STATION = "station_to_station"
    TEMPORAL_CONTEXT = "temporal_context"
    PICK_TO_STATION = "pick_to_station"
    PICK_TO_EVENT = "pick_to_event"
    EVENT_TO_STATION = "event_to_station"
    TRAVEL_TIME_REFERENCE = "travel_time_reference"


@dataclass(frozen=True, slots=True)
class GraphNode:
    """A typed node with optional spatial coordinates."""

    node_id: str
    node_type: GraphNodeType
    features: dict[str, MetadataValue] = field(default_factory=dict)
    coordinates: Coordinate3D | None = None
    metadata: dict[str, MetadataValue] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class GraphEdge:
    """A directed relation between two graph nodes."""

    source_id: str
    target_id: str
    edge_type: GraphEdgeType
    features: dict[str, MetadataValue] = field(default_factory=dict)
    metadata: dict[str, MetadataValue] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class GraphExample:
    """A graph-structured training example for multi-station tasks."""

    task: SeismologyTask
    nodes: tuple[GraphNode, ...]
    edges: tuple[GraphEdge, ...]
    global_features: dict[str, MetadataValue] = field(default_factory=dict)
    target_description: str = ""
    metadata: dict[str, MetadataValue] = field(default_factory=dict)

    def __post_init__(self) -> None:
        node_ids = {node.node_id for node in self.nodes}
        if len(node_ids) != len(self.nodes):
            msg = "graph node identifiers must be unique"
            raise ValueError(msg)
        for edge in self.edges:
            if edge.source_id not in node_ids or edge.target_id not in node_ids:
                msg = "graph edges must reference existing node identifiers"
                raise ValueError(msg)
