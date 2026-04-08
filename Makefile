.PHONY: sync lint format typecheck test check clean

sync:
	uv sync

lint:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	uv run mypy src tests

test:
	uv run pytest

check:
	uv run ruff check .
	uv run ruff format --check .
	uv run mypy src tests
	uv run pytest

clean:
	rm -rf .mypy_cache .pytest_cache .ruff_cache htmlcov .coverage dist build
