# 2023 Day 17: Clumsy Crucible

Mode: practice · clock started 2026-11-25T23:57:34+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `674` | 0:02:03 | — | 0 |
| 2 | `773` | 0:04:24 | 42s | 0 |

## Approach
Part 1: Dijkstra over (row, col, axis of the next move). From each state, move 1..3 blocks along the axis in either direction, then switch axis.
Part 2: Same search with run lengths 4..10; the target only counts when reached at the end of a legal run, which this formulation gives for free.

## Log
- Recognised the puzzle from training data, including the part 2 rule (min 4, max 10 straight), so part 2 was drafted before it unlocked. It was submitted only after reading the real part 2 text and matching both examples (94 and 71).
- Part 1 submit took over two minutes to return because of the tool's cross-process throttle; the Bash call hit its 120 s timeout and had to be waited on in the background.
- No wrong answers.
