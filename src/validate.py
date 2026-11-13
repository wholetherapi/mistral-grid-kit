#!/usr/bin/env python3
"""Validation checks shipped with the Mistral Grid kit."""

import json
import sys
from pathlib import Path


REQUIRED_FIELDS = {'volume', 'primary', 'backup'}


def validate_plan(path: Path) -> list[str]:
    errors: list[str] = []
    payload = json.loads(path.read_text(encoding='utf-8'))
    missing = REQUIRED_FIELDS - payload.keys()
    if missing:
        errors.append(f'plan is missing fields: {sorted(missing)}')
    primary = payload.get('primary') or {}
    for field in ('code', 'latency_ms', 'capacity', 'cost_per_unit'):
        if field not in primary:
            errors.append(f'primary region lacks {field}')
    if payload.get('volume', 0) <= 0:
        errors.append('volume must be positive')
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print('usage: validate.py PLAN.json')
        return 2
    errors = validate_plan(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f'ERROR: {error}')
        return 1
    print('plan OK')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
