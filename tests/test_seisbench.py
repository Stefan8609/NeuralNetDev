"""Tests for SeisBench exploration helpers."""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np
from _pytest.monkeypatch import MonkeyPatch

from seismo_nn.seisbench import configure_local_seisbench_environment, sample_to_waveform_window


def test_configure_local_seisbench_environment_uses_repo_local_paths(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.delenv("SEISBENCH_CACHE_ROOT", raising=False)
    monkeypatch.delenv("MPLCONFIGDIR", raising=False)
    monkeypatch.delenv("XDG_CACHE_HOME", raising=False)

    environment = configure_local_seisbench_environment(tmp_path)

    assert environment.cache_root == (tmp_path / ".seisbench-cache").resolve()
    assert environment.datasets_root == environment.cache_root / "datasets"
    assert environment.matplotlib_config_dir == (tmp_path / ".mplconfig").resolve()
    assert environment.xdg_cache_home == (tmp_path / ".cache").resolve()
    assert environment.cache_root.is_dir()
    assert environment.matplotlib_config_dir.is_dir()
    assert environment.xdg_cache_home.is_dir()
    assert (environment.xdg_cache_home / "fontconfig").is_dir()
    assert os.environ["SEISBENCH_CACHE_ROOT"] == str(environment.cache_root)
    assert os.environ["MPLCONFIGDIR"] == str(environment.matplotlib_config_dir)
    assert os.environ["XDG_CACHE_HOME"] == str(environment.xdg_cache_home)


def test_sample_to_waveform_window_maps_core_metadata_fields() -> None:
    samples = np.zeros((3, 200), dtype=np.float32)
    metadata = {
        "trace_sampling_rate_hz": 100.0,
        "trace_component_order": "ZNE",
        "station_network_code": "XX",
        "station_code": "ABCD",
        "source_id": "event-001",
        "trace_p_arrival_sample": 42,
    }

    window = sample_to_waveform_window(samples, metadata)

    assert window.samples.dtype == np.float64
    assert window.sample_rate_hz == 100.0
    assert window.channel_order == ("Z", "N", "E")
    assert window.station_code == "XX.ABCD"
    assert window.event_id == "event-001"
    assert window.metadata["trace_p_arrival_sample"] == 42
