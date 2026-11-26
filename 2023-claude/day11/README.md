# 2023 Day 11: Cosmic Expansion

Mode: practice · clock started 2026-11-25T23:57:49+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `9543156` | 0:01:03 | — | 0 |
| 2 | `625243292686` | 0:03:00 | — | 0 |

## Approach
Part 1: Galaxy coordinates are remapped per axis, adding (factor - 1) for each empty row/column before them; the pairwise Manhattan sum splits into independent per-axis sums, computed in O(n log n) with sorted prefix sums.
Part 2: Same function with factor 1,000,000 (example checked at factors 10 and 100).

## Log
- The owner had already solved both parts, so `submit` checked answers against the site's recorded ones.
- No wrong attempts. I recognised this puzzle from training data (the factor-of-a-million part 2 is well known), which affects the benchmark.
- The part 2 submit waited in the tool's cross-process queue for about two minutes even though it only compared against a stored answer.
