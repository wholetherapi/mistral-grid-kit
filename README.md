# Mistral Grid Launch Kit

Released reference implementation for the Mistral Grid launch kit.

The kit ships the routing-grid planner and the validation harness used by the field teams. Everything in this repository is public and covered by the Apache-2.0 license.

## Contents

- `src/` - planner implementation and unit checks.
- `data/` - example region matrices used in the quick start.
- `experiments/` - benchmark notes and calibration runs.

## Quick start

    python src/planner.py --grid data/regions.csv --out build/plan.json

## Release notes

The initial public release includes the planner, the CSV loaders, and the benchmark script. UI tooling is planned for a later release.
