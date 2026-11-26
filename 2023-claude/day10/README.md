# 2023 Day 10: Pipe Maze

Mode: practice · clock started 2026-11-25T23:57:13+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `7093` | 0:01:03 | — | 0 |
| 2 | `407` | 0:03:00 | — | 0 |

## Approach
Part 1: Infer the shape of the S tile from its neighbours, walk the loop, and take half its length.
Part 2: Scan each row with an even-odd crossing rule, toggling on loop tiles that connect north (|, L, J). Non-loop tiles seen while the toggle is set are inside.

## Log
- Recognised the puzzle from training data (well-known 2023 day 10); used the standard crossing-count approach.
- All examples matched on the first run; both answers were correct on the first try.
- The owner had already solved both parts, so submit checked against the recorded answers.
- The part 2 submit sat in the cross-process queue for about two minutes before it returned.
