#!/usr/bin/env python3
"""Routing-grid planner for the Mistral Grid launch kit."""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


@dataclass
class Region:
    code: str
    latency_ms: float
    capacity: int
    cost_per_unit: float


def load_regions(path: Path) -> list[Region]:
    regions: list[Region] = []
    with path.open(newline='', encoding='utf-8') as handle:
        for row in csv.DictReader(handle):
            regions.append(
                Region(
                    code=row['code'],
                    latency_ms=float(row['latency_ms']),
                    capacity=int(row['capacity']),
                    cost_per_unit=float(row['cost_per_unit']),
                )
            )
    return regions


def score(region: Region, volume: int) -> float:
    overflow = max(0, volume - region.capacity)
    return region.latency_ms + region.cost_per_unit * volume + overflow * 2.5


def plan(regions: Iterable[Region], volume: int) -> dict:
    candidates = sorted(regions, key=lambda item: score(item, volume))
    primary = candidates[0]
    backup = candidates[1] if len(candidates) > 1 else None
    return {
        'volume': volume,
        'primary': asdict(primary),
        'backup': asdict(backup) if backup else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--grid', required=True)
    parser.add_argument('--volume', type=int, default=1200)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    regions = load_regions(Path(args.grid))
    result = plan(regions, args.volume)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
