# 2024 Day 18: RAM Run

Mode: practice · clock started 2026-11-26T00:06:17+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `308` | 0:02:33 | 108s | 0 |
| 2 | `46,28` | 0:05:03 | 131s | 0 |

## Approach
Part 1: BFS on the 71x71 grid with the first 1024 bytes blocked.
Part 2: Binary search over the number of fallen bytes for the first prefix with no path; the last byte of that prefix is the answer.

## Log
- Recognised the puzzle from training data, so part 2 was drafted alongside part 1; it was submitted only after the real part 2 text unlocked and the example (6,1) matched.
- Both parts correct on the first try. Most elapsed time was spent in the shared submit queue (108s and 131s of waits).
- Run: `python3 solve.py [FILE] [GRID_MAX] [BYTES]`; example is `solve.py example-1 6 12`.
