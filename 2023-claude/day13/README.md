# 2023 Day 13: Point of Incidence

Mode: practice · clock started 2026-11-25T23:57:31+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `33047` | 0:01:00 | — | 0 |
| 2 | `28806` | 0:02:57 | — | 0 |

## Approach
Part 1: For each candidate horizontal split, count mismatched cells between mirrored row pairs; a split with 0 mismatches is the reflection. Columns are handled by transposing.
Part 2: Same scan, but look for a split with exactly 1 mismatch (the smudge), which is automatically a different line from part 1's.

## Log
- Recognised the puzzle from training data; used the mismatch-count trick directly.
- Both parts matched the examples (405, 400) and were correct on the first attempt. The owner had already solved both parts, so submit checked against the recorded answers.
- Part 2's "submit" sat in the tool's cross-process queue for about two minutes even though it was only a local check against the recorded answer; most of the part 2 time is that wait.
