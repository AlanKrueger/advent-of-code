# 2025 Day 8: Playground

| Part | Answer | Time from start | Wrong attempts |
|------|--------|-----------------|----------------|
| 1 | `66640` | 0:00:20 | 0 |
| 2 | `78894156` | 0:00:50 | 0 |

## Approach
Part 1: Sort all ~500k point pairs by squared distance, union-find the 1000 shortest pairs
(10 for the 20-point example), multiply the three largest component sizes.
Part 2: Keep unioning along the sorted pairs until one component remains; multiply the
X coordinates of the pair that made the final merge.

## Log
- Both parts matched the examples first try.
- The first part 2 submit hit the site's "answer too recently" cooldown (2s left),
  likely from parallel runs on other days sharing the account; retried after a few seconds.
