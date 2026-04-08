"""Contract tests for project navigation and domain scaffolding."""

import numpy as np
import pytest

from seismo_nn.config import CONFIGS_ROOT, DOCS_ROOT, PROJECT_ROOT, SRC_ROOT, TESTS_ROOT
from seismo_nn.pipeline import (
    GraphEdge,
    GraphEdgeType,
    GraphExample,
    GraphNode,
    GraphNodeType,
    WaveformWindow,
    WindowSpec,
)
from seismo_nn.tasks import DEFAULT_TASK_SPECS, LabelKind, SeismologyTask, StructureKind
from seismo_nn.training import TrainingConfig


def test_project_paths_exist() -> None:
    assert PROJECT_ROOT.exists()
    assert SRC_ROOT.exists()
    assert TESTS_ROOT.exists()
    assert CONFIGS_ROOT.exists()
    assert DOCS_ROOT.exists()


def test_default_task_specs_cover_core_tasks() -> None:
    tasks = {spec.task for spec in DEFAULT_TASK_SPECS}
    label_kinds = {spec.label_kind for spec in DEFAULT_TASK_SPECS}
    structure_kinds = {spec.structure_kind for spec in DEFAULT_TASK_SPECS}

    assert SeismologyTask.PHASE_PICKING in tasks
    assert SeismologyTask.EVENT_DETECTION in tasks
    assert SeismologyTask.EVENT_ASSOCIATION in tasks
    assert SeismologyTask.EARTHQUAKE_LOCATING in tasks
    assert LabelKind.POINT in label_kinds
    assert StructureKind.EVENT_STATION_BIPARTITE in structure_kinds
    assert StructureKind.GEOMETRIC in structure_kinds


def test_window_spec_rejects_invalid_values() -> None:
    with pytest.raises(ValueError, match="sample_rate_hz must be positive"):
        WindowSpec(sample_rate_hz=0.0, duration_seconds=30.0, stride_seconds=5.0)


def test_waveform_window_requires_channel_count_match() -> None:
    with pytest.raises(ValueError, match="channel_order length must match"):
        WaveformWindow(
            task=SeismologyTask.PHASE_PICKING,
            samples=np.zeros((2, 16), dtype=np.float64),
            sample_rate_hz=100.0,
            station_code="AAA",
            channel_order=("Z", "N", "E"),
        )


def test_graph_example_rejects_missing_edge_nodes() -> None:
    node = GraphNode(node_id="station_a", node_type=GraphNodeType.STATION)
    edge = GraphEdge(
        source_id="station_a",
        target_id="station_b",
        edge_type=GraphEdgeType.STATION_TO_STATION,
    )

    with pytest.raises(ValueError, match="graph edges must reference existing node identifiers"):
        GraphExample(
            task=SeismologyTask.MULTI_STATION_INTERPRETATION,
            nodes=(node,),
            edges=(edge,),
        )


def test_training_config_requires_normalized_splits() -> None:
    with pytest.raises(ValueError, match=r"splits must sum to 1\.0"):
        TrainingConfig(
            task=SeismologyTask.PHASE_PICKING,
            train_split=0.7,
            validation_split=0.2,
            test_split=0.2,
        )
