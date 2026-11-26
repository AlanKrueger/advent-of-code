# 2023 Day 14: Parabolic Reflector Dish

Mode: practice · clock started 2026-11-25T23:57:52+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `108955` | 0:01:09 | — | 0 |
| 2 | `106689` | 0:03:00 | — | 0 |

## Approach
Part 1: Slide each column's round rocks north to just below the nearest cube rock (or the edge) and sum the row weights.
Part 2: One spin cycle is four rounds of "tilt north, rotate clockwise". Store each grid state, find where the cycle repeats, and index into the history to get the state after 1e9 cycles.

## Log
- Recognised the puzzle from training data (well-known tilt + cycle-detection problem).
- Both examples matched on the first run (136, 64); both answers were correct on the first attempt. The owner had already solved this day, so the tool checked against the recorded answers.
- Most of the wall-clock time went to waiting in the shared request queue behind other parallel runs.
