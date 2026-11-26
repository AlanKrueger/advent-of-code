# 2023 Day 15: Lens Library

Mode: practice · clock started 2026-11-25T23:57:16+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `511215` | 0:01:03 | — | 0 |
| 2 | `236057` | 0:03:00 | — | 0 |

## Approach
Part 1: Sum the HASH (`(v + ord(c)) * 17 % 256`) of each comma-separated step.
Part 2: 256 boxes as insertion-ordered dicts; `=` sets or replaces a label in place, `-` pops it. Sum (box+1) * slot * focal length.

## Log
- Both parts were already solved by hand on the site, so `fetch` showed both parts and `submit` checked against the recorded answers.
- Both examples matched (1320, 145) on the first run; both answers correct first try.
- Recognised the puzzle from training data (well-known HASH/HASHMAP day).
- Part 2 was ready at about 0:01; most of the 0:03:00 was spent queued behind about 20 parallel runs sharing the request throttle.
