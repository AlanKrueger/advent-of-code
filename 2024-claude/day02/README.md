# 2024 Day 2: Red-Nosed Reports

Mode: practice · clock started 2026-11-26T00:04:41+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `549` | 0:00:11 | — | 0 |
| 2 | `589` | 0:00:11 | — | 0 |

## Approach
Part 1: A report is safe if all adjacent differences are in 1..3 or all are in -3..-1.
Part 2: Brute force: a report is safe if removing any single level makes it safe under the part 1 rule.

## Log
- Owner had already solved both parts, so the fetched puzzle.md contained both parts; both submits were checked against the site's recorded answers.
- Recognised the puzzle from training data (well-known 2024 day 2).
- Both examples matched (2, 4) and both answers were correct on the first try.
