# 2025 Day 3: Lobby

Mode: practice · clock started 2026-11-25T23:31:44+00:00

| Part | Answer | Time from start | Wrong attempts |
|------|--------|-----------------|----------------|
| 1 | `17087` | 0:00:31 | 0 |
| 2 | `169019504359949` | 0:01:16 | 0 |

## Approach
Part 1: For each bank of digits, pick the largest 2-digit number keeping order, using a greedy choice of the largest digit that still leaves room for the remaining picks.
Part 2: Same greedy with 12 digits instead of 2.

## Log
- Wrote the greedy for general k in part 1, so part 2 was a one-line change.
- Both parts hit "You gave an answer too recently" (exit 2) on the first submit because other agents were submitting on the same account in parallel. Part 2 took two failed retries before going through; roughly 40 s of the part 2 time is that waiting.
- This puzzle is from before the model's training cutoff, so the time is optimistic compared with an unseen puzzle.
