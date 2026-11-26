# 2023 Day 1: Trebuchet?!

Mode: practice · clock started 2026-11-25T23:56:58+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `53921` | 0:01:00 | — | 0 |
| 2 | `54676` | 0:02:51 | — | 0 |

## Approach
Part 1: For each line, take the first and last digit character and sum the two-digit numbers.
Part 2: Scan every position, accepting a digit character or a spelled-out digit word starting there, so overlapping words like "eightwo" give both 8 and 2.

## Log
- Recognised the puzzle from training data, including the overlapping-word trap in part 2.
- The owner had already solved both parts, so both answers were checked against the site's recorded answers. Both examples matched first try.
- Part 2's check took about 1m50s because roughly 20 parallel runs were queued on the 3-second request throttle.
