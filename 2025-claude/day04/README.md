# 2025 Day 4: Printing Department

Mode: practice · clock started 2026-11-25T23:31:42+00:00

| Part | Answer | Time from start | Wrong attempts |
|------|--------|-----------------|----------------|
| 1 | `1449` | 0:00:27 | 0 |
| 2 | `8746` | 0:00:57 | 0 |

## Approach
Part 1: Store roll positions in a set and count rolls with fewer than four of their eight neighbours occupied.
Part 2: Repeatedly remove every accessible roll until none remain accessible, and count the total removed. Runs in about 0.5 s.

## Log
- Both parts matched the example and were accepted on the first submission.
- Each submission first hit the site's "answered too recently" throttle (exit 2, 2 s left) because other agents were submitting other days on the same account; a retry a few seconds later went through.
