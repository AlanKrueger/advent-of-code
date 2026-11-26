# 2023 Day 12: Hot Springs

Mode: practice · clock started 2026-11-25T23:56:13+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `7771` | 0:01:06 | — | 0 |
| 2 | `10861030975833` | 0:04:21 | 27s | 0 |

## Approach
Part 1: Memoised recursion over (position, group index): either treat the current cell as operational, or place the next whole group there if it fits and is followed by a non-`#`.
Part 2: Same function on the rows unfolded five times; memoisation keeps it fast.

## Log
- Recognised the puzzle from training data (well-known memoised DP).
- The owner had already solved part 1 by hand, so the puzzle page showed both parts at fetch time and one solver was written for both. Both examples (21, 525152) matched on the first run and both answers were correct first time.
- The part 2 submit took about 3 minutes of wall time, of which the report counts 27s as cooldown. The rest was presumably spent waiting in the cross-process submit queue.
