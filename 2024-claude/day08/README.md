# 2024 Day 8: Resonant Collinearity

Mode: practice · clock started 2026-11-26T00:04:29+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `280` | 0:02:30 | 69s | 0 |
| 2 | `958` | 0:05:36 | 132s | 0 |

## Approach
Part 1: Group antennas by frequency; for each pair, add the two points that extend the pair's offset beyond each end, if in bounds.
Part 2: For each pair, walk the line through both antennas in both directions (step = offset reduced by gcd) and collect every in-bounds point.

## Log
- Recognised the puzzle from training data, so part 2 was drafted before it unlocked; it was submitted only after reading the part 2 text and matching its 34 example.
- The T-only part 2 diagram (example-6) gives 23 when run directly because its `#` marks are parsed as antennas; that diagram is not a clean input. The 34 example matched.
- Both parts correct on first submit. Most of the elapsed time was waiting in the shared submit queue.
