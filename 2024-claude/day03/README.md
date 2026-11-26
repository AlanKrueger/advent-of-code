# 2024 Day 3: Mull It Over

Mode: practice · clock started 2026-11-26T00:04:53+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `171183089` | 0:00:11 | — | 0 |
| 2 | `63866497` | 0:00:17 | — | 0 |

## Approach
Part 1: Regex for `mul(X,Y)` with 1-3 digit operands, summing the products.
Part 2: The same regex also matches `do()` and `don't()`, which toggle whether later products count.

## Log
- The owner had already solved both parts by hand, so both parts were visible at fetch time and one solver handled both.
- Both examples matched (161 and 48), and both answers were accepted on the first submit.
- I recognised this puzzle from training data.
