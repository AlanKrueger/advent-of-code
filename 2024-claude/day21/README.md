# 2024 Day 21: Keypad Conundrum

Mode: practice · clock started 2026-11-26T00:07:05+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `242484` | 0:02:48 | 126s | 0 |
| 2 | `294209504640384` | 0:04:56 | 106s | 0 |

## Approach
Part 1: For each pair of keys, enumerate the move orderings that never touch the gap, each ending in `A`. A memoized `cost(segment, depth)` takes the cheapest expansion of every key-to-key move one layer down, and each layer starts again at `A`. The numeric keypad sits on top with 2 directional robots below it.
Part 2: The same function with 25 robots.

## Log
- Recognised the puzzle from training data (the standard memoized-depth solution), so part 2 was written with part 1 as a robot-count parameter.
- The example (`example-4`) gave 126384 as expected. Both parts were correct first try. Part 2 has no example answer to check against.
- Most of the elapsed time went to the shared submit queue and cooldown waits (about 230 s in total).
