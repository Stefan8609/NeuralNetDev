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
from seismo_nn.seisbench import (
    SeisBenchEnvironment,
    available_seisbench_dataset_names,
    configure_local_seisbench_environment,
    dataset_summary,
    load_seisbench_dataset,
    metadata_preview,
    sample_to_waveform_window,
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
    "SeisBenchEnvironment",
    "SeismologyTask",
    "Station",
    "StructureKind",
    "TaskSpec",
    "TrainingConfig",
    "TrainingRunSummary",
    "WaveformWindow",
    "WindowSpec",
    "__version__",
    "available_seisbench_dataset_names",
    "configure_local_seisbench_environment",
    "dataset_summary",
    "load_seisbench_dataset",
    "metadata_preview",
    "sample_to_waveform_window",
]
__version__ = "0.1.0"
