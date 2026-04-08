"""Helpers for exploring SeisBench datasets without leaking notebook logic into the package."""

from __future__ import annotations

import inspect
import os
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from seismo_nn.config import PROJECT_ROOT
from seismo_nn.pipeline import WaveformWindow
from seismo_nn.tasks import SeismologyTask


@dataclass(frozen=True, slots=True)
class SeisBenchEnvironment:
    """Filesystem locations used to keep SeisBench exploration local to the repository."""

    cache_root: Path
    datasets_root: Path
    matplotlib_config_dir: Path
    xdg_cache_home: Path


def configure_local_seisbench_environment(
    project_root: Path | str | None = None,
) -> SeisBenchEnvironment:
    """Point SeisBench and plotting caches into the repository for reproducible local work."""

    root = Path(project_root) if project_root is not None else PROJECT_ROOT
    desired_cache_root = root / ".seisbench-cache"
    desired_matplotlib_dir = root / ".mplconfig"
    desired_xdg_cache_home = root / ".cache"

    os.environ.setdefault("SEISBENCH_CACHE_ROOT", str(desired_cache_root))
    os.environ.setdefault("MPLCONFIGDIR", str(desired_matplotlib_dir))
    os.environ.setdefault("XDG_CACHE_HOME", str(desired_xdg_cache_home))

    cache_root = Path(os.environ["SEISBENCH_CACHE_ROOT"]).expanduser().resolve()
    matplotlib_config_dir = Path(os.environ["MPLCONFIGDIR"]).expanduser().resolve()
    xdg_cache_home = Path(os.environ["XDG_CACHE_HOME"]).expanduser().resolve()

    cache_root.mkdir(parents=True, exist_ok=True)
    matplotlib_config_dir.mkdir(parents=True, exist_ok=True)
    xdg_cache_home.mkdir(parents=True, exist_ok=True)
    (xdg_cache_home / "fontconfig").mkdir(parents=True, exist_ok=True)

    return SeisBenchEnvironment(
        cache_root=cache_root,
        datasets_root=cache_root / "datasets",
        matplotlib_config_dir=matplotlib_config_dir,
        xdg_cache_home=xdg_cache_home,
    )


def _import_seisbench_data_module() -> Any:
    configure_local_seisbench_environment()
    import seisbench.data as sbd

    return sbd


def available_seisbench_dataset_names() -> tuple[str, ...]:
    """Return concrete SeisBench dataset classes that are useful for interactive exploration."""

    sbd = _import_seisbench_data_module()
    base_class = sbd.WaveformDataset
    excluded_names = {
        "AbstractBenchmarkDataset",
        "BenchmarkDataset",
        "Bucketer",
        "DASBenchmarkDataset",
        "DASDataWriter",
        "DASDataset",
        "DatasetInspection",
        "GeometricBucketer",
        "MultiDASDataset",
        "MultiWaveformDataset",
        "RandomDASDataset",
        "WaveformBenchmarkDataset",
        "WaveformDataWriter",
        "WaveformDataset",
    }

    dataset_names: list[str] = []
    for name in getattr(sbd, "__all__", []):
        if name in excluded_names:
            continue
        candidate = getattr(sbd, name, None)
        if inspect.isclass(candidate) and issubclass(candidate, base_class):
            dataset_names.append(name)

    return tuple(sorted(dataset_names))


def load_seisbench_dataset(dataset_name: str, **kwargs: Any) -> Any:
    """Instantiate a SeisBench dataset after configuring local cache locations."""

    sbd = _import_seisbench_data_module()
    try:
        dataset_cls = getattr(sbd, dataset_name)
    except AttributeError as exc:
        available = ", ".join(available_seisbench_dataset_names())
        msg = f"Unknown SeisBench dataset '{dataset_name}'. Available datasets: {available}"
        raise ValueError(msg) from exc

    return dataset_cls(**kwargs)


def dataset_summary(dataset: Any) -> dict[str, object]:
    """Build a small summary dictionary that works well in notebooks."""

    metadata = dataset.metadata
    summary: dict[str, object] = {
        "name": getattr(dataset, "name", dataset.__class__.__name__),
        "n_traces": len(dataset),
        "n_metadata_columns": len(metadata.columns),
        "metadata_columns": tuple(str(column) for column in metadata.columns[:12]),
    }

    if getattr(dataset, "sampling_rate", None) is not None:
        summary["sampling_rate_hz"] = float(dataset.sampling_rate)
    if getattr(dataset, "component_order", None) is not None:
        summary["component_order"] = tuple(str(component) for component in dataset.component_order)
    if "split" in metadata.columns:
        summary["split_counts"] = {
            str(name): int(count) for name, count in metadata["split"].value_counts().items()
        }

    return summary


def metadata_preview(dataset: Any, limit: int = 5) -> pd.DataFrame:
    """Return a shallow copy of the first few metadata rows for display."""

    return dataset.metadata.head(limit).copy()


def sample_to_waveform_window(
    samples: np.ndarray,
    metadata: Mapping[str, object],
    task: SeismologyTask = SeismologyTask.PHASE_PICKING,
) -> WaveformWindow:
    """Convert a SeisBench sample into the repository's explicit waveform schema."""

    sample_array = np.asarray(samples, dtype=np.float64)
    if sample_array.ndim != 2:
        msg = "samples must have shape (channels, samples)"
        raise ValueError(msg)

    channel_order = _channel_order_from_metadata(metadata)
    if len(channel_order) != sample_array.shape[0]:
        msg = "trace_component_order does not match the waveform channel dimension"
        raise ValueError(msg)

    sample_rate_hz = _sample_rate_from_metadata(metadata)
    station_code = _station_code_from_metadata(metadata)
    event_id = _optional_text(metadata, ("source_id", "event_id", "trace_name"))

    return WaveformWindow(
        task=task,
        samples=sample_array,
        sample_rate_hz=sample_rate_hz,
        station_code=station_code,
        event_id=event_id,
        channel_order=channel_order,
        metadata={str(key): _to_metadata_value(value) for key, value in metadata.items()},
    )


def _channel_order_from_metadata(metadata: Mapping[str, object]) -> tuple[str, ...]:
    value = metadata.get("trace_component_order", "ZNE")
    if isinstance(value, str):
        return tuple(value)
    if isinstance(value, tuple | list):
        return tuple(str(component) for component in value)
    return tuple(str(value))


def _sample_rate_from_metadata(metadata: Mapping[str, object]) -> float:
    value = metadata.get("trace_sampling_rate_hz")
    if value is None:
        msg = "metadata must include trace_sampling_rate_hz"
        raise ValueError(msg)
    if isinstance(value, bool | str):
        return float(value)
    if isinstance(value, int | float):
        return float(value)
    if hasattr(value, "item"):
        item = value.item()
        if isinstance(item, bool | int | float | str):
            return float(item)
    msg = "trace_sampling_rate_hz must be numeric"
    raise ValueError(msg)


def _station_code_from_metadata(metadata: Mapping[str, object]) -> str:
    network = _optional_text(metadata, ("station_network_code",))
    station = _optional_text(metadata, ("station_code",))
    if network and station:
        return f"{network}.{station}"
    if station:
        return station
    return "UNKNOWN"


def _optional_text(metadata: Mapping[str, object], keys: tuple[str, ...]) -> str | None:
    for key in keys:
        value = metadata.get(key)
        if value is None:
            continue
        text = str(value).strip()
        if text and text.lower() != "nan":
            return text
    return None


def _to_metadata_value(value: object) -> str | float | int | bool:
    if isinstance(value, bool | int | float | str):
        return value
    if hasattr(value, "item"):
        item = value.item()
        if isinstance(item, bool | int | float | str):
            return item
    if isinstance(value, pd.Timestamp):
        return str(value.isoformat())
    return str(value)
