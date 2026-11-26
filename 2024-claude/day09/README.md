# 2024 Day 9: Disk Fragmenter

Mode: practice · clock started 2026-11-26T00:04:20+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `6395800119709` | 0:01:33 | 24s | 0 |
| 2 | `6418529470362` | 0:04:21 | 108s | 0 |

## Approach
Part 1: Expand the map into a block list and swap blocks with two pointers (leftmost gap, rightmost file block), then sum position times ID.
Part 2: Keep files and gaps as (start, length) lists. For each file from highest ID down, take the first gap left of it that is long enough and shrink that gap. Runs in about 2 s with a linear gap scan.

## Log
- Recognised the puzzle from training data, so part 2 was drafted before it unlocked. It was submitted only after the real part 2 text and its example (2858) matched.
- Both parts were correct on the first try. Most of the elapsed time was spent in the shared submit queue (24 s and 108 s).
