# Development notes

## Branching

A simple starting strategy:
- `main`: protected, always passing CI
- feature branches: one branch per task
- squash-merge PRs to keep history clean

## Commit style

Recommended commit prefixes:
- `feat:` new functionality
- `fix:` bug fix
- `refactor:` internal cleanup
- `test:` test changes
- `docs:` documentation
- `chore:` tooling or maintenance

## Suggested conventions for ML work

Keep these concerns separate early:
- raw data access
- preprocessing
- model definition
- training loop
- evaluation
- experiment configs
- notebooks only for exploration, not core logic
