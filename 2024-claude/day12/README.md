# 2024 Day 12: Garden Groups

Mode: practice · clock started 2026-11-26T00:04:59+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `1371306` | 0:03:09 | 135s | 0 |
| 2 | `805880` | 0:06:02 | 134s | 0 |

## Approach
Part 1: Flood-fill each region; perimeter is the count of (cell, direction) boundary edges; sum area * perimeter.
Part 2: A side is a run of boundary edges with the same direction; count an edge only when its predecessor along the run (left for horizontal edges, up for vertical edges) is not also a boundary edge.

## Log
- Recognised the puzzle from training data (part 2 counts sides), so part 2 was drafted alongside part 1 and checked against the remembered example values. It was submitted only after the real part 2 text unlocked and its examples (80, 436, 236, 368, 1206) all matched.
- Both parts correct first try. Most of the elapsed time was the shared submit queue and cooldown waits (about 135 s per part).
