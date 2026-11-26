# 2024 Day 16: Reindeer Maze

Mode: practice · clock started 2026-11-26T00:04:47+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `135512` | 0:02:51 | 114s | 0 |
| 2 | `541` | 0:05:54 | 141s | 0 |

## Approach
Part 1: Dijkstra over (row, col, facing) states; forward step costs 1, a 90-degree turn costs 1000.
Part 2: A second Dijkstra from E (all facings) on reversed states; a tile is on a best path when forward distance plus backward distance to the reversed state equals the best score.

## Log
- Recognised the puzzle from training data, so part 2 was drafted before it unlocked and only submitted after the real text and both examples (45, 64) matched.
- Both parts correct on the first submit. Most of the elapsed time was the shared submit queue and cooldown waits.
