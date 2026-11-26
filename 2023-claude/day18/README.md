# 2023 Day 18: Lavaduct Lagoon

Mode: practice · clock started 2026-11-25T23:57:07+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `47139` | 0:01:00 | — | 0 |
| 2 | `173152345887206` | 0:04:15 | 57s | 0 |

## Approach
Part 1: Walk the polygon vertices, take the shoelace area, and add the boundary with Pick's theorem (area + perimeter/2 + 1).
Part 2: Same function, with distance and direction decoded from the hex code (5 hex digits of distance, last digit 0-3 = RDLU).

## Log
- Recognised the puzzle from training data (shoelace + Pick's is the well-known approach).
- Both parts matched the examples first try; both answers correct on first submit.
- The site recorded part 1 as solved by the owner, so part 1 was checked against the recorded answer. Part 2 was a real submit and waited 57s for the site's cooldown.
