#!/usr/bin/env bash
set -euo pipefail

uv sync
uv run pre-commit install
uv run pre-commit install --hook-type pre-push

echo "Project bootstrapped successfully."
