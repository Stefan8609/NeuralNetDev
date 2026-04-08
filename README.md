# seismo-nn

A clean, maintainable Python scaffold for seismology neural network development.

This template is designed for:
- isolated environments via `uv`
- reproducible dependency management
- `src/` layout for cleaner imports and packaging
- automated linting, formatting, type checking, and tests
- Git hooks with `pre-commit`
- GitHub Actions continuous integration

## Project layout

```text
seismo-nn/
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
├── scripts/
├── src/
│   └── seismo_nn/
│       ├── __init__.py
│       └── config.py
├── tests/
│   └── test_import.py
├── .editorconfig
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── Makefile
├── pyproject.toml
└── README.md
```

## Recommended workflow

### 1. Initialize the repository

```bash
git init
```

### 2. Create and sync the environment

```bash
uv sync
```

This will create a local `.venv` and install the default dependency groups.

### 3. Activate the environment

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Git hooks

```bash
uv run pre-commit install
uv run pre-commit install --hook-type pre-push
```

### 5. Run quality checks

```bash
uv run ruff check .
uv run ruff format .
uv run mypy src tests
uv run pytest
```

Or use:

```bash
make check
```

## Dependency management

Add a runtime dependency:

```bash
uv add obspy
```

Add a development dependency:

```bash
uv add --dev jupyter
```

Upgrade and refresh the lockfile:

```bash
uv lock
uv sync
```

## Suggested next dependencies for your use case

Depending on your first milestone, you may want to add some of these later:
- `obspy`
- `pandas`
- `matplotlib`
- `scipy`
- `torch`
- `lightning`
- `seisbench`
- `jupyterlab`
- `hydra-core` or `pydantic-settings`

I would add these only when the workflow truly needs them.

## First development targets

A clean first milestone would be:
1. dataset ingestion
2. preprocessing and windowing
3. baseline model training
4. evaluation metrics
5. experiment configuration and reproducibility

## Naming notes

The package is currently named `seismo_nn` and the project is named `seismo-nn`.
If you want a different repository or package name, update:
- `project.name` in `pyproject.toml`
- `src/seismo_nn/`
- imports in `tests/`

## Common commands

```bash
make sync      # install / update environment
make lint      # run ruff lint
make format    # run ruff formatter
make typecheck # run mypy
make test      # run pytest
make check     # run all checks
```

## License

This template ships with the MIT License. Replace it if needed.
