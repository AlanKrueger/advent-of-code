# 2023 Day 25: Snowverload

Mode: practice · clock started 2026-11-26T00:01:34+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `548960` | 0:00:57 | 21s | 0 |
| 2 | `0` | 0:04:04 | 36s | 0 |

## Approach
Part 1: Build an undirected graph with networkx, take `minimum_edge_cut` (size 3), remove it, and multiply the two component sizes.
Part 2: Free star that needs all 49 other stars; left for the coordinator to claim once the other days are done.

## Log
- Recognised the puzzle from training data (global min cut of size 3).
- The sample input is `example-2`; `example-1` is the reset-screen text block. First run against `example-1` crashed on an empty graph; `example-2` gave 54 as expected.
- Part 1 correct on the first submission.

- Part 2 (the free final star) was claimed by the coordinator once all 49 other 2023 stars were in; its time is not a solve time.
