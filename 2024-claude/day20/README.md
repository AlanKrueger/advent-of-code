# 2024 Day 20: Race Condition

Mode: practice · clock started 2026-11-26T00:06:26+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `1499` | 0:03:00 | 120s | 0 |
| 2 | `1027164` | 0:05:16 | 109s | 0 |

## Approach
Part 1: BFS from the start gives the distance along the single track to every track cell. A cheat from cell a to cell b within Manhattan distance 2 saves dist[b] - dist[a] - |a-b|; count pairs saving at least 100.
Part 2: Same pair count with Manhattan radius 20 (about 1.5 s for both parts).

## Log
- Recognised the puzzle from training data, so part 2 (radius 20) was written alongside part 1 and checked against the part 2 example (285 cheats saving at least 50) once its text was unlocked.
- Part 1 example histogram matched exactly; both answers correct first try.
- `python3 solve.py [FILE] [THRESHOLD] [h]`: the third argument prints the savings histogram.
