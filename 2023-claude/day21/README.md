# 2023 Day 21: Step Counter

Mode: practice · clock started 2026-11-26T00:01:19+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `3770` | 0:00:24 | — | 0 |
| 2 | `628206330073385` | 0:00:54 | 15s | 0 |

## Approach
Part 1: BFS from `S` recording each cell's distance; count cells with distance <= 64 and the same parity as 64.
Part 2: the same BFS on the infinitely tiled grid (coordinates taken mod the size). The real input has a clear row and column through `S` and the target is 65 + 202300 * 131, so the count is quadratic in the number of tiles crossed. Count directly at 65, 196 and 327 steps and extrapolate with Newton forward differences.

## Log
- Recognised the puzzle from training data (the quadratic-fit trick for part 2).
- Checked the infinite-grid BFS against the example values for 6, 10, 50, 100 and 500 steps (`python3 solve.py example-1 6 N`). The example grid lacks the clear-row structure, so the quadratic shortcut was only applied to the real input.
- Both parts correct first try. The owner had already solved one part by hand.
