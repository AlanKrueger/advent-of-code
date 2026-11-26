# 2024 Day 15: Warehouse Woes

Mode: practice · clock started 2026-11-26T00:04:50+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `1499739` | 0:03:03 | 126s | 0 |
| 2 | `1522215` | 0:05:57 | 147s | 0 |

## Approach
Part 1: Simulate the robot on a dict grid. For each move, collect the robot plus every box in the push chain; if any of them would hit a wall, skip the move, otherwise shift them all one step.
Part 2: Widen the map, then run the same simulation. For vertical moves the chain search is a BFS that adds the other half of each `[]` box it meets. GPS uses the `[` cell.

## Log
- I recognised the puzzle from training data, so I drafted part 2 before it unlocked. I submitted it only after the real part 2 text confirmed the example answer of 9021.
- Both examples (10092, 2028) matched first time. No wrong answers.
- Most of the elapsed time was spent waiting in the shared submit queue and cooldown.
