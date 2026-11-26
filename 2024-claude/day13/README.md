# 2024 Day 13: Claw Contraption

Mode: practice · clock started 2026-11-26T00:05:02+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `29598` | 0:03:18 | 141s | 0 |
| 2 | `93217456941970` | 0:06:05 | 137s | 0 |

## Approach
Part 1: Each machine is a 2x2 linear system; solve with Cramer's rule and keep only non-negative integer solutions (at most 100 presses), costing 3 per A and 1 per B.
Part 2: Same solver with 10^13 added to each prize coordinate and no press limit.

## Log
- Recognised the puzzle from training data (I knew part 2 adds 10000000000000 to the prize coordinates), so part 2 was drafted before it unlocked and submitted only after reading its text.
- Example part 1 matched (480) on the first run.
- Part 2 example: only machines 2 and 4 win, as the text says. Both answers were accepted on the first try.
