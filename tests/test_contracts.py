"""Contract tests for project navigation and domain scaffolding."""

from seismo_nn.config import PROJECT_ROOT, SRC_ROOT, TESTS_ROOT
from seismo_nn.tasks import DEFAULT_TASK_SPECS, LabelKind, SeismologyTask


def test_project_paths_exist() -> None:
    assert PROJECT_ROOT.exists()
    assert SRC_ROOT.exists()
    assert TESTS_ROOT.exists()


def test_default_task_specs_cover_core_tasks() -> None:
    tasks = {spec.task for spec in DEFAULT_TASK_SPECS}
    label_kinds = {spec.label_kind for spec in DEFAULT_TASK_SPECS}

    assert SeismologyTask.PHASE_PICKING in tasks
    assert SeismologyTask.EVENT_DETECTION in tasks
    assert LabelKind.POINT in label_kinds
