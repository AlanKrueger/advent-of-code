# 2023 Day 3: Gear Ratios

Mode: practice · clock started 2026-11-25T23:57:28+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `556057` | 0:01:00 | — | 0 |
| 2 | `82824352` | 0:02:57 | — | 0 |

## Approach
Part 1: Find each number with a regex, scan the box around it, and sum the numbers that touch any non-digit, non-`.` character.
Part 2: In the same scan, record each number against every adjacent `*`; sum the products for stars with exactly two numbers.

## Log
- The owner had already solved both parts, so the page showed both parts at once and both were written in one pass. Both example answers matched (4361, 467835). Both submits were checked against the recorded answers and were correct on the first try.
- I recognised the puzzle from training data.
- The part 2 submit took about two minutes, most likely the tool's cross-process throttle, so the part 2 time is mostly waiting.
