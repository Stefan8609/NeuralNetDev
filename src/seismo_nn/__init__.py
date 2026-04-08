"""Core package for seismo_nn."""

from seismo_nn.evaluation import EvaluationSummary, MetricRecord
from seismo_nn.models import ModelFamily, ModelSpec
from seismo_nn.pipeline import (
    GraphEdge,
    GraphEdgeType,
    GraphExample,
    GraphNode,
    GraphNodeType,
    NormalizationSpec,
    PickObservation,
    Station,
    WaveformWindow,
    WindowSpec,
)
from seismo_nn.tasks import DEFAULT_TASK_SPECS, LabelKind, SeismologyTask, StructureKind, TaskSpec
from seismo_nn.training import TrainingConfig, TrainingRunSummary

__all__ = [
    "DEFAULT_TASK_SPECS",
    "EvaluationSummary",
    "GraphEdge",
    "GraphEdgeType",
    "GraphExample",
    "GraphNode",
    "GraphNodeType",
    "LabelKind",
    "MetricRecord",
    "ModelFamily",
    "ModelSpec",
    "NormalizationSpec",
    "PickObservation",
    "SeismologyTask",
    "Station",
    "StructureKind",
    "TaskSpec",
    "TrainingConfig",
    "TrainingRunSummary",
    "WaveformWindow",
    "WindowSpec",
    "__version__",
]
__version__ = "0.1.0"
