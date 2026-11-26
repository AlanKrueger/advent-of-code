# 2023 Day 8: Haunted Wasteland

Mode: practice · clock started 2026-11-25T23:57:46+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `18157` | 0:01:00 | — | 0 |
| 2 | `14299763833181` | 0:03:00 | — | 0 |

## Approach
Part 1: Walk from AAA following the repeating L/R instructions until reaching ZZZ.
Part 2: Count steps from each `..A` node to its first `..Z` node and take the LCM of those counts. This relies on the input's cycles being aligned (first Z hit equals cycle length), which holds for AoC inputs.

## Log
- Recognised the puzzle from training data (the LCM shortcut is well known), so this run is not a blind solve.
- Owner had already solved both parts; the tool checked answers against the recorded ones. Both matched on the first try.
- The part 2 submit sat in the tool's cross-process throttle for about two minutes; most of the part 2 time is that wait.
