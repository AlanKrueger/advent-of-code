# 2023 Day 7: Camel Cards

Mode: practice · clock started 2026-11-25T23:57:22+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `250898830` | 0:01:00 | — | 0 |
| 2 | `252127335` | 0:04:15 | 63s | 0 |

## Approach
Part 1: Sort hands by (descending card-count multiset, card ranks in order) and sum bid times rank.
Part 2: Remove jokers, add their count to the largest group, and rank J lowest for tie-breaks.

## Log
- Recognised the puzzle from training data.
- The owner had already solved part 1, so the fetch showed both parts at once. I wrote both parts together, and both matched the examples (6440, 5905).
- Part 1 was checked against the site's recorded answer. Part 2 was submitted for real and accepted after a 63 s cooldown wait.
