"""Basic smoke tests for the project scaffold."""

from seismo_nn import __version__


def test_version_is_string() -> None:
    assert isinstance(__version__, str)
