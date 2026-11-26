# 2024 Day 6: Guard Gallivant

Mode: practice · clock started 2026-11-26T00:04:23+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `4433` | 0:02:09 | 51s | 0 |
| 2 | `1516` | 0:05:18 | 120s | 0 |

## Approach
Part 1: Simulate the guard (turn right at `#`, else step) and count distinct cells visited until she leaves the grid.
Part 2: For each cell on the part 1 path except the start, add an obstruction there and re-simulate. A repeated (row, col, direction) state means a loop. Brute force runs in about 5 s.

## Log
- I recognised the puzzle from training data, so I drafted part 2 alongside part 1. I submitted it only after reading the real part 2 text and matching its example (6).
- Both parts were correct on the first submission.
