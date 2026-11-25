# 2025 Day 9: Movie Theater

Mode: practice · clock started 2026-11-25T23:31:43+00:00

| Part | Answer | Time from start | Wrong attempts |
|------|--------|-----------------|----------------|
| 1 | `4786902990` | 0:00:38 | 0 |
| 2 | `1571016172` | 0:00:50 | 0 |

## Approach
Part 1: Brute force over all pairs of red tiles, maximizing the inclusive rectangle area.
Part 2: Compress coordinates (each distinct x/y is a cell, plus a gap cell between neighbours), draw the polygon edges, flood-fill the outside, and use a 2D prefix sum over outside cells to reject any candidate rectangle that touches the outside. Runs in about 0.4 s.

## Log
- Wrote both parts before submitting part 1, guessing the part 2 rule (rectangle must stay inside the loop). The example gave 50 and 24, matching both stated answers.
- First part 1 submit was rate-limited (another run on the same account had just submitted); retried after the 2 s wait.
