# 2023 Day 19: Aplenty

Mode: practice · clock started 2026-11-25T23:57:55+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `472630` | 0:01:12 | — | 0 |
| 2 | `116738260946855` | 0:03:54 | 45s | 0 |

## Approach
Part 1: Parse the workflows and run each part through them from `in`, summing ratings of accepted parts.
Part 2: Recurse from `in` with a 4-D box of rating ranges, splitting the box at each rule into the matching and non-matching halves, and sum box volumes that reach `A`.

## Log
- Recognised the puzzle from training data (standard range-splitting solution).
- The fetch showed part 1 was already solved on the site, so puzzle.md had both parts up front; wrote both parts together and both matched the examples first try.
- Part 1 submit was checked against the site's recorded answer; part 2 was a real submit and waited about 45s on the shared cooldown queue.
