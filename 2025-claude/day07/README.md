# 2025 Day 7: Laboratories

Mode: practice · clock started 2026-11-25T23:31:43+00:00

| Part | Answer | Time from start | Wrong attempts |
|------|--------|-----------------|----------------|
| 1 | `1518` | 0:00:26 | 0 |
| 2 | `25489586715621` | 0:00:38 | 0 |

## Approach
Part 1: Sweep rows top to bottom keeping the set of beam columns; a beam on a `^` counts one split and moves to the two neighbouring columns (merging duplicates).
Part 2: Same sweep, but each column carries a count of timelines; splitting adds the count to both neighbours, and the answer is the total count after the last row.

## Log
- Wrote both parts in one pass (guessed part 2 would ask for path counts). Example matched 21 and 40.
- First part 1 submit hit exit 2 ("answer too recently, 2s left"), likely another agent's submission on the shared account; retried immediately and it was accepted.
