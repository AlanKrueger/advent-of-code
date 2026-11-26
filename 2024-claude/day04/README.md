# 2024 Day 4: Ceres Search

Mode: practice · clock started 2026-11-26T00:04:44+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `2575` | 0:00:11 | — | 0 |
| 2 | `2041` | 0:00:17 | — | 0 |

## Approach
Part 1: From every cell, try all 8 directions and count where the next four letters spell XMAS.
Part 2: For every `A`, check that both diagonal pairs of neighbours are exactly {M, S}.

## Log
- Recognised the puzzle from training data before reading it; wrote both parts at once.
- Owner had already solved both parts by hand, so both parts were visible at fetch and submits were checked against the recorded answers.
- Sample input is `example-2` (18 / 9); both parts matched first time and were accepted with no wrong attempts.
