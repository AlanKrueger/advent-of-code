# 2025 Day 2: Gift Shop

Mode: practice · clock started 2026-11-25T23:31:43+00:00

| Part | Answer | Time from start | Wrong attempts |
|------|--------|-----------------|----------------|
| 1 | `30608905813` | 0:00:20 | 0 |
| 2 | `31898925685` | 0:00:32 | 0 |

## Approach
Part 1: Generate every number made of a digit block repeated exactly twice, up to the longest bound's length, and sum those that fall in any range.
Part 2: Same generation with any repeat count of at least two, deduplicated with a set (e.g. 222222 arises from blocks 2, 22 and 222).

## Log
- Wrote both parts up front, guessing part 2 would generalize the repeat count. Both examples matched; both answers accepted first try.
