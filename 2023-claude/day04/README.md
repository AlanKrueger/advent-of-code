# 2023 Day 4: Scratchcards

Mode: practice · clock started 2026-11-25T23:57:40+00:00
| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `25010` | 0:01:00 | — | 0 |
| 2 | `9924412` | 0:03:00 | — | 0 |

## Approach
Part 1: Count each card's matches (set intersection of winning and held numbers) and score 2^(matches-1).
Part 2: Keep a copy count per card and walk the cards in order, adding each card's count to the next `matches` cards.

## Log
- The owner had already solved both parts, so both parts were visible at fetch and `submit` checked the answers against the site. Both matched the examples (13, 30) and were correct on the first try.
- I recognised the puzzle from training data.
- Most of the elapsed time was spent waiting on the shared request throttle: about 17 parallel runs were each re-fetching their day page in `submit`.
