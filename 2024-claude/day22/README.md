# 2024 Day 22: Monkey Market

Mode: practice · clock started 2026-11-26T00:07:14+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `19877757850` | 0:03:09 | 147s | 0 |
| 2 | `2399` | 0:04:59 | 92s | 0 |

## Approach
Part 1: Simulate the shift/xor/mod generator 2000 steps per buyer and sum the final secrets.
Part 2: For each buyer, record the price after the first occurrence of every 4-change window,
add it to a global table keyed by the window, and take the maximum total.

## Log
- Recognised the puzzle from training data, so part 2 was drafted before it unlocked. It was
  submitted only after the part 2 text was read and its example (1, 2, 3, 2024 -> 23) matched.
- Part 2's example list (1, 2, 3, 2024) differs from part 1's (1, 10, 100, 2024) and is not
  saved as an example file before part 2 unlocks, so a scratch copy was used to check it.
- Both parts correct on the first try. Most of the elapsed time was spent waiting in the
  shared submit queue/cooldown (147 s + 92 s).
