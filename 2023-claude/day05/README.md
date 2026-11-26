# 2023 Day 5: If You Give A Seed A Fertilizer

Mode: practice · clock started 2026-11-25T23:57:10+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `1181555926` | 0:01:03 | — | 0 |
| 2 | `37806486` | 0:03:00 | — | 0 |

## Approach
Part 1: Treat each seed as a one-element interval and push it through the seven maps.
Part 2: Same code on the seed ranges; each map splits an interval into the overlapping
piece (shifted) and the leftover pieces (retried against the other rules, or passed
through unchanged). Answer is the smallest interval start at the end.

## Log
- Recognised the puzzle from training data (well-known interval-splitting day).
- Owner had already solved both parts, so the full text was visible at fetch and
  `submit` checked against the recorded answers. Both correct first try.
- Part 1 was confirmed at about 1:03. The part 2 submit then sat in the tool's
  cross-process queue/throttle for roughly two minutes, which is why part 2 shows 3:00.
