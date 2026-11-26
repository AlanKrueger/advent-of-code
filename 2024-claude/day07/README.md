# 2024 Day 7: Bridge Repair

Mode: practice · clock started 2026-11-26T00:03:35+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `14711933466277` | 0:01:36 | — | 0 |
| 2 | `286580387663654` | 0:05:00 | 150s | 0 |

## Approach
Part 1: Recurse backwards from the test value over the numbers right to left: undo `+` by subtraction and `*` by exact division, pruning impossible branches.
Part 2: Add undoing concatenation by stripping the last number's digits off the target's suffix.

## Log
- Recognised the puzzle from training data (including part 2's concatenation operator), so both parts were written together before part 2 unlocked; part 2 was submitted only after reading its text and matching the example (11387).
- Both examples matched on the first run; both answers correct first try.
- Part 2's time includes 150 s waiting on the site cooldown / other runs' submits.
