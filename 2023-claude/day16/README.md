# 2023 Day 16: The Floor Will Be Lava

Mode: practice · clock started 2026-11-25T23:57:04+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `6622` | 0:01:00 | — | 0 |
| 2 | `7130` | 0:02:54 | — | 0 |

## Approach
Part 1: Run a DFS over (row, col, direction) states with a seen set, applying the mirror and splitter rules, and count the distinct cells visited.
Part 2: Repeat that from every edge cell heading inward and take the maximum. Takes about 1.3 s.

## Log
- The owner had already solved both parts, so `submit` checked the answers against the site's recorded ones.
- I recognised the puzzle from training data. It is a standard beam simulation.
- Both example answers (46 and 51) matched on the first run. Both answers were correct, with no wrong attempts.
- The part 2 submit sat in the tool's cross-process throttle for about 2 minutes. That accounts for most of part 2's time.
