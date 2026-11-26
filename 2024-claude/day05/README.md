# 2024 Day 5: Print Queue

Mode: practice · clock started 2026-11-26T00:04:56+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `4662` | 0:03:03 | 138s | 0 |
| 2 | `5900` | 0:05:58 | 144s | 0 |

## Approach
Part 1: Store the `X|Y` rules as a set of pairs and use them as a comparator; an update is
correct if sorting it with that comparator leaves it unchanged. Sum the middle pages.
Part 2: For the updates that sorting changed, sum the middle page of the sorted version.

## Log
- Recognised the puzzle from training data, so part 2 (reorder the bad updates) was drafted
  alongside part 1; it was submitted only after the real part 2 text and its example (123) matched.
- Both examples matched first time (143, 123); no wrong answers.
- Most of the elapsed time was spent in the shared submit queue (about 140 s per part).
