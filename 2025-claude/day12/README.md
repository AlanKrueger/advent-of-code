# 2025 Day 12: Christmas Tree Farm

Mode: practice · clock started 2026-11-25T23:31:42+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `448` | 0:03:05 | — | 0 |
| 2 | `0` | 0:04:20 | — | 0 |

## Approach
Part 1: For each region, reject it if the presents' total cell count exceeds the area, and accept it if the number of presents is at most (w//3)*(h//3), since each present fits in its own 3x3 box. Regions between those bounds get an exact backtracking search that fills the first undecided cell with a present or leaves it empty while slack remains. Every region in the real input is settled by the two bounds (552 too big, 448 trivially fit), so the input runs instantly. The example needs the search and takes about 13 s.
Part 2: The free final star, which needs all 23 other 2025 stars. The coordinator claimed it (a form posting `level=2`, `answer=0`) after days 2–11 finished, so its time in the table is not a solve time.

## Log
- The first exact search placed pieces in a fixed order at any position. It ran for over 2 minutes on the example's infeasible third region, so I replaced it with a first-empty-cell search.
- Part 1 was accepted on the first submission.
