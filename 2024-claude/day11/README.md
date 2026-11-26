# 2024 Day 11: Plutonian Pebbles

Mode: practice · clock started 2026-11-26T00:04:26+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `186175` | 0:01:45 | 36s | 0 |
| 2 | `220566831337810` | 0:04:42 | 114s | 0 |

## Approach
Part 1: Order doesn't affect the count, so keep a Counter of stone value -> multiplicity and apply the rules per distinct value for 25 blinks.
Part 2: Same code for 75 blinks; the number of distinct values stays small.

## Log
- Recognised the puzzle from training data; wrote the counter approach directly, so part 2 was drafted before it unlocked and submitted after reading its text.
- The only code block (`example-1`) is a multi-step trace, not an input; tested with `example-input` containing `125 17` (expected 55312 after 25 blinks, matched).
- Both parts correct first try. Most of the elapsed time was the shared submit queue.
