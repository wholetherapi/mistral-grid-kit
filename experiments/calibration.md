# Calibration notes - Mistral Grid

Baseline run on 2026-08-11 with a synthetic volume of 1,200 parcels.

- Planner chose NWC as primary and CEN as backup.
- Mean planning latency: 84 ms over 500 iterations.
- Overflow penalty kept secondary regions below 4% of volume.

Larger volumes above 3,000 should use the split-plan variant described in the internal design note.
