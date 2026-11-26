# 2023 Day 6: Wait For It

Mode: practice · clock started 2026-11-25T23:57:25+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `2065338` | 0:01:00 | — | 0 |
| 2 | `34934171` | 0:02:57 | — | 0 |

## Approach
Part 1: For each race, count hold times h with h*(T-h) > D. The bounds come from the quadratic's roots, computed with `isqrt` and then adjusted to exact integers. Multiply the counts together.
Part 2: Join the digits on each line into a single race and use the same count.

## Log
- I recognised the puzzle from training data. Both parts matched their examples on the first run.
- The owner had already solved both parts, so `submit` checked my answers against the site's recorded answers. Both were correct.
- About two of the minutes before part 2 was confirmed were spent waiting on the part 2 `submit` call, which printed nothing while it waited (probably the cross-process throttle).
