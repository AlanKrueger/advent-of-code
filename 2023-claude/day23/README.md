# 2023 Day 23: A Long Walk

Mode: practice · clock started 2026-11-26T00:01:31+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `1998` | 0:00:33 | — | 0 |
| 2 | `6434` | 0:01:06 | 21s | 0 |

## Approach
Part 1: Compress the grid into a graph of junctions (cells with 3+ open neighbours, plus start and end), walking corridors while respecting slopes, then brute-force DFS for the longest simple path with a bitmask of visited junctions.
Part 2: Same graph with slopes ignored. The end has a single incoming junction, so the DFS stops there and adds the final edge, which prunes dead branches. Runs in about 5 s.

## Log
- Recognised the puzzle from training data (junction compression plus longest-path DFS is the known approach).
- Both parts wrote in one pass; example matched (94, 154); both answers correct first try.
- The owner had already solved part 1 by hand, so puzzle.md showed both parts at fetch time.
