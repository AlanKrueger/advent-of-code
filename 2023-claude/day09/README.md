# 2023 Day 9: Mirage Maintenance

Mode: practice · clock started 2026-11-25T23:57:37+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `1861775706` | 0:00:57 | — | 0 |
| 2 | `1082` | 0:02:54 | — | 0 |

## Approach
Part 1: Recursively take successive differences until all zero; the next value is the last element plus the extrapolated next value of the difference row.
Part 2: Same function applied to the reversed sequence gives the previous value.

## Log
- Recognised the puzzle from training data (repeated finite differences; reversing the row for part 2).
- Both parts had already been solved by the owner, so `submit` checked against the site's recorded answers. Both correct on the first try.
- Part 2's check sat for about two minutes queued behind the cross-process request throttle shared with parallel runs.
