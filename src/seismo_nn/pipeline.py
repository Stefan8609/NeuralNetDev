"""Data-facing schemas for seismic ML pipelines."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from numpy.typing import NDArray

from seismo_nn.tasks import SeismologyTask

WaveformArray = NDArray[np.float64]


@dataclass(frozen=True, slots=True)
class WindowSpec:
    """Defines how waveform windows are constructed."""

    sample_rate_hz: float
    duration_seconds: float
    stride_seconds: float
    channels: tuple[str, ...] = ("Z", "N", "E")


@dataclass(frozen=True, slots=True)
class WaveformWindow:
    """A fixed-size waveform segment and its metadata."""

    task: SeismologyTask
    samples: WaveformArray
    sample_rate_hz: float
    station_code: str
    event_id: str | None = None
    channel_order: tuple[str, ...] = ("Z", "N", "E")
    metadata: dict[str, str | float | int] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class NormalizationSpec:
    """Preprocessing configuration applied before model input."""

    demean: bool = True
    detrend: bool = False
    peak_normalize: bool = True
    clip_value: float | None = None
