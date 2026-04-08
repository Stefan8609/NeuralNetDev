# seismo-nn

A maintainable research scaffold for seismology machine learning that can grow from
simple waveform baselines to graph neural networks and geometric deep learning methods.

The repository includes:
- explicit task definitions for waveform, graph, and geometry-aware problems
- typed schemas for waveform windows, stations, picks, and graph examples
- lightweight model, training, and evaluation contracts
- manifest files that help human contributors and coding agents navigate quickly

This project is designed for:
- Python 3.11 and `uv`
- reproducible dependency management
- `src/` layout for reusable package code
- `configs/` for experiment-facing configuration
- `ruff`, `pytest`, and `pre-commit`
- clear architecture before framework-heavy model implementation

## Project layout

```text
seismo-nn/
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DEVELOPMENT.md
│   ├── MANIFEST.md
│   └── ROADMAP.md
├── configs/
│   └── MANIFEST.md
├── scripts/
├── src/
│   └── seismo_nn/
│       ├── __init__.py
│       └── config.py
│       ├── evaluation.py
│       ├── MANIFEST.md
│       ├── models.py
│       ├── pipeline.py
│       ├── tasks.py
│       └── training.py
├── tests/
│   ├── MANIFEST.md
│   └── test_import.py
├── AGENTS.md
├── MANIFEST.md
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

## Navigation

Start here when orienting to the project:
- `MANIFEST.md`
- `AGENTS.md`
- `docs/ARCHITECTURE.md`
- `docs/ROADMAP.md`

## Scientific direction

The scaffold is meant to support:
- phase picking
- denoising
- event detection and association
- earthquake locating
- travel-time consistency modeling
- multi-station waveform interpretation

When proposing or implementing a method, keep these scientific questions explicit:
- what are the nodes
- what are the edges
- which features encode waveform, timing, and geometry
- what are the targets and losses
- which physical constraints or uncertainties matter

## First development targets

A clean first milestone would be:
1. dataset ingestion
2. preprocessing and windowing
3. one simple waveform baseline
4. one graph-ready multi-station representation
5. experiment configuration and reproducibility

The strongest first applied target is usually either:
- phase picking
- event detection

Both are represented in the package task definitions, with graph/geometric follow-ons
documented for later milestones.

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
