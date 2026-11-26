# 2023 Day 22: Sand Slabs

Mode: practice · clock started 2026-11-26T00:01:25+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `461` | 0:00:42 | 12s | 0 |
| 2 | `74074` | 0:01:18 | 9s | 0 |

## Approach
Part 1: Sort bricks by lowest z and drop each onto a height map of (x,y) -> (top z, brick id), recording which bricks support which. A brick is safe to remove if every brick it supports has at least two supporters.
Part 2: For each brick, BFS upward: a brick falls once all of its supporters have fallen. Sum the fallen counts excluding the removed brick.

## Log
- Recognised the puzzle from training data, so part 2 (chain-reaction sum) was drafted together with part 1 and checked against the part 2 example (7) after it unlocked.
- Both answers correct on the first submission.
