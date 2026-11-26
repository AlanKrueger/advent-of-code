# 2023 Day 2: Cube Conundrum

Mode: practice · clock started 2026-11-25T23:57:43+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `2720` | 0:01:00 | — | 0 |
| 2 | `71535` | 0:03:00 | — | 0 |

## Approach
Part 1: For each game take the per-colour maximum over all draws; sum IDs of games whose maxima fit within 12 red, 13 green, 14 blue.
Part 2: Sum the product of those per-colour maxima.

## Log
- The owner had already solved both parts, so both parts were visible at fetch and `submit` checked against the recorded answers.
- Both examples matched (8, 2286) on the first run; both answers correct first try.
- Recognised the puzzle from training data (2023 day 2 is well known); the solution is short either way.
- The part 2 check took about 2 minutes to return, waiting in the tool's cross-process submit queue, even though it made no real submission.
