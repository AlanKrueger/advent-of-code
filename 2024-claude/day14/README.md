# 2024 Day 14: Restroom Redoubt

Mode: practice · clock started 2026-11-26T00:04:38+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `228410028` | 0:02:45 | 93s | 0 |
| 2 | `8258` | 0:05:57 | 141s | 0 |

## Approach
Part 1: Each robot's position after t seconds is `(p + v*t) mod size`; count robots per quadrant at t=100 and multiply.
Part 2: Scan t over one full period (101*103) for the first step where no two robots share a tile; `-v` prints the grid to confirm it is the tree picture.

## Log
- Recognised the puzzle from training data, including the known heuristic that the tree frame is the first step with all positions distinct. Checked the printed grid (a long run of `#` rows forming the frame) before submitting.
- Example matched (12) on the first try; both parts correct first submit. Most elapsed time was the shared submit queue and cooldown.
