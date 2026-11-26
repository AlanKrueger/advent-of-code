# 2023 Day 24: Never Tell Me The Odds

Mode: practice · clock started 2026-11-26T00:01:28+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `15318` | 0:00:51 | 18s | 0 |
| 2 | `870379016024859` | 0:01:21 | 12s | 0 |

## Approach
Part 1: For every pair, solve the 2x2 system for both hailstones' times with exact fractions; count pairs where both times are non-negative and the crossing point lies inside the test area.
Part 2: The rock condition (P - p_i) x (V - v_i) = 0 has the nonlinear term P x V in common for all hailstones, so subtracting it for pairs of hailstones gives linear equations in the six unknowns. Three pairs from the first three hailstones give 9 equations; Gauss-Jordan elimination over Fractions solves them exactly.

## Log
- Recognised the puzzle from training data (well-known 2023 day 24), including the part 2 cross-product linearisation trick. Part 2 was drafted before it unlocked and submitted only after reading its text and matching the example (47).
- Both parts correct on the first try.
