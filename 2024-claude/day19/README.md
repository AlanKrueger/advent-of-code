# 2024 Day 19: Linen Layout

Mode: practice · clock started 2026-11-26T00:06:20+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `209` | 0:02:42 | 117s | 0 |
| 2 | `777669668613191` | 0:05:07 | 120s | 0 |

## Approach
Part 1: For each design, a suffix DP over positions counts the ways to tile it with towel patterns; a design is possible if the count is nonzero.
Part 2: Sum the same counts.

## Log
- Recognised the puzzle from training data, so part 2 (count the arrangements) was written alongside part 1 and checked against the part 2 example (16) once it unlocked.
- Both answers were correct on the first try. Most of the elapsed time was the shared submit queue and cooldown waits.
