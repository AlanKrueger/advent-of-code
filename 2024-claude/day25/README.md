# 2024 Day 25: Code Chronicle

Mode: practice · clock started 2026-11-26T00:09:20+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `3451` | 0:02:13 | 112s | 0 |
| 2 | `0` | 0:03:26 | — | 0 |

## Approach
Part 1: Parse each schematic as a set of `#` cells; top row filled means lock, otherwise key. Count lock/key pairs whose cell sets are disjoint.
Part 2: Free final star that needs all 49 other stars; left for the coordinator to claim once the other days are done.

## Log
- Recognised the puzzle from training data (lock/key schematics, count non-overlapping pairs).
- Example gave 3 as expected; first submission correct.
- Most of the 2:13 was the shared submit queue waiting on other runs (112s reported as cooldown waits).

- Part 2 (the free final star) was claimed by the coordinator once all 49 other 2024 stars were in; its time is not a solve time.
