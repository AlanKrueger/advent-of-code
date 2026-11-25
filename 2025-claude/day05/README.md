# 2025 Day 5: Cafeteria

| Part | Answer | Time from start | Wrong attempts |
|------|--------|-----------------|----------------|
| 1 | `756` | 0:00:32 | 0 |
| 2 | `355555479253787` | 0:00:43 | 0 |

## Approach
Part 1: For each available ID, check whether any inclusive range contains it.
Part 2: Sort the ranges, merge overlapping or adjacent ones, and sum the merged lengths.

## Log
- Both parts written before the first submission (part 2 guessed from the input shape); both example answers matched (3 and 14).
- The first part 1 submit returned "answered too recently" (exit 2), most likely because another agent submitted on the same account moments before. The retry a few seconds later was accepted.
