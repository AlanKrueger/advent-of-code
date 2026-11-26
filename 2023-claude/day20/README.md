# 2023 Day 20: Pulse Propagation

Mode: practice · clock started 2026-11-25T23:57:01+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `680278040` | 0:01:00 | — | 0 |
| 2 | `243548140870057` | 0:04:00 | 39s | 0 |

## Approach
Part 1: Simulate the pulse queue (BFS order) for 1000 presses, counting low and high pulses.
Part 2: `rx` is fed by a single conjunction whose inputs are independent counters; record the first press on which each input sends a high pulse into the feeder, and take the LCM.

## Log
- Recognised the puzzle from training data (the LCM-of-feeder-cycles trick for part 2 is the well-known solution).
- Owner had already solved part 1 by hand; the tool checked my part 1 against the recorded answer. Part 2 was a real submission.
- Both examples matched on the first run; no wrong answers. Part 2 has no example, so only the real input was checked.
