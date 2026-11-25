# 2025 Day 1: Secret Entrance

Mode: practice · clock started 2026-11-25T22:58:19+00:00

| Part | Answer | Time from start | Wrong attempts |
|------|--------|-----------------|----------------|
| 1 | `1052` | 0:00:13 | 0 |
| 2 | `6295` | 0:00:27 | 0 |

## Approach
Part 1: Apply each L/R rotation to a dial position mod 100 and count rotations that end on 0.
Part 2: Step the dial one click at a time and count every click that lands on 0, so passes during a rotation count too. Brute force runs in under 0.1 s.

## Log
- First end-to-end test of `tools/aoc.py` and the `/aoc` skill. Fetch, example check, and both submissions worked on the first try.
- This puzzle is from before the model's training cutoff, so the time is optimistic compared with an unseen puzzle.
