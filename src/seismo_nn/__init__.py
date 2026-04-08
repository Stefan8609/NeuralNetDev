"""Core package for seismo_nn."""

from seismo_nn.evaluation import EvaluationSummary, MetricRecord
from seismo_nn.models import ModelSpec
from seismo_nn.pipeline import NormalizationSpec, WaveformWindow, WindowSpec
from seismo_nn.tasks import DEFAULT_TASK_SPECS, LabelKind, SeismologyTask, TaskSpec
from seismo_nn.training import TrainingConfig, TrainingRunSummary

__all__ = [
    "DEFAULT_TASK_SPECS",
    "EvaluationSummary",
    "LabelKind",
    "MetricRecord",
    "ModelSpec",
    "NormalizationSpec",
    "SeismologyTask",
    "TaskSpec",
    "TrainingConfig",
    "TrainingRunSummary",
    "WaveformWindow",
    "WindowSpec",
    "__version__",
]
__version__ = "0.1.0"
