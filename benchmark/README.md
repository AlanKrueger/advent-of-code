# Benchmark: hand-solved vs Claude

Snapshot taken 2026-11-25. Your numbers come from the stats pages in
`2023-human-stats.txt` and `2024-human-stats.txt` (time from midnight unlock) and,
as a rough active-time estimate, from the gaps between consecutive commits in one
sitting (`human-commit-times.txt`). Claude's numbers come from each
`<year>-claude/dayNN/log.json`.

## How to read this

- **Claude's times here measure the pipeline, not problem solving.** These puzzles
  predate the model's training data, and every agent said it recognised its puzzle.
  The last edit to `solve.py` landed a median of 7 seconds after the
  puzzle and input were on disk. A fair speed comparison needs puzzles the model
  hasn't seen, which means the live 2026 runs.
- **Claude's submit times are inflated by running 20 days in parallel.** All agents
  shared one account, so submits waited on each other and on the site's cooldown
  between answers. "Net" subtracts the waits the tool logged. For 2023 days 1–20,
  time in the shared request throttle wasn't logged yet, so those net times are
  upper bounds; the "code done" column is the better guide there.
- **Your stats-page times count from midnight**, so ">24h" mostly means you started
  on a later day. The commit-gap estimate is closer to active time, but it exists
  only where you committed consecutive days in one sitting, and a gap may include
  breaks.

## 2023

| Day | You: stats p1 / p2 | You: commit-gap estimate | Claude: code done | Claude: net p1 / p2 | Claude: logged waits |
|----:|--------------------|--------------------------|------------------:|---------------------|---------------------:|
| 1 | >24h / >24h | — | 0:05 | 1:00 / 2:51 | 0:00 |
| 2 | >24h / >24h | 1:30:12 | 0:05 | 1:00 / 3:00 | 0:00 |
| 3 | >24h / >24h | — | 0:06 | 1:00 / 2:57 | 0:00 |
| 4 | >24h / >24h | — | 0:05 | 1:00 / 3:00 | 0:00 |
| 5 | >24h / >24h | 1:47:23 | 0:07 | 1:03 / 3:00 | 0:00 |
| 6 | >24h / >24h | 1:18:53 | 0:08 | 1:00 / 2:57 | 0:00 |
| 7 | >24h / - | — | 0:06 | 1:00 / 3:12 | 1:03 |
| 8 | 18:07:16 / >24h | 1:32:43 | 0:06 | 1:00 / 3:00 | 0:00 |
| 9 | 03:35:56 / 03:40:14 | — | 0:05 | 0:57 / 2:54 | 0:00 |
| 10 | 22:01:03 / >24h | — | 0:09 | 1:03 / 3:00 | 0:00 |
| 11 | 02:55:08 / 02:59:14 | 1:02:55 | 0:07 | 1:03 / 3:00 | 0:00 |
| 12 | >24h / - | — | 0:06 | 1:06 / 3:54 | 0:27 |
| 13 | >24h / >24h | 1:53:46 | 0:06 | 1:00 / 2:57 | 0:00 |
| 14 | >24h / >24h | 1:52:53 | 0:07 | 1:09 / 3:00 | 0:00 |
| 15 | >24h / >24h | 34:24 | 0:06 | 1:03 / 3:00 | 0:00 |
| 16 | >24h / >24h | 1:10:40 | 0:07 | 1:00 / 2:54 | 0:00 |
| 17 | — / — | — | 0:08 | 2:03 / 3:42 | 0:42 |
| 18 | >24h / - | 1:41:50 (part1) | 0:06 | 1:00 / 3:18 | 0:57 |
| 19 | >24h / - | — | 0:08 | 1:12 / 3:09 | 0:45 |
| 20 | >24h / - | 1:37:23 (part 1 only) | 0:10 | 1:00 / 3:21 | 0:39 |
| 21 | >24h / - | — | 0:10 | 0:24 / 0:39 | 0:15 |
| 22 | — / — | — | 0:09 | 0:30 / 0:57 | 0:21 |
| 23 | >24h / - | — | 0:10 | 0:33 / 0:45 | 0:21 |
| 24 | — / — | — | 0:15 | 0:33 / 0:51 | 0:30 |
| 25 | — / — | — | 0:05 | 0:36 / bonus | 0:57 |

## 2024

| Day | You: stats p1 / p2 | You: commit-gap estimate | Claude: code done | Claude: net p1 / p2 | Claude: logged waits |
|----:|--------------------|--------------------------|------------------:|---------------------|---------------------:|
| 1 | >24h / >24h | — | 0:06 | 0:11 / 0:11 | 0:00 |
| 2 | 20:10:37 / >24h | — | 0:05 | 0:11 / 0:11 | 0:00 |
| 3 | >24h / >24h | — | 0:06 | 0:11 / 0:17 | 0:00 |
| 4 | >24h / >24h | 45:41 | 0:06 | 0:11 / 0:17 | 0:00 |
| 5 | — / — | — | 0:06 | 0:45 / 1:16 | 4:42 |
| 6 | — / — | — | 0:08 | 1:18 / 2:27 | 2:51 |
| 7 | — / — | — | 0:06 | 1:36 / 2:30 | 2:30 |
| 8 | — / — | — | 0:08 | 1:21 / 2:15 | 3:21 |
| 9 | — / — | — | 0:08 | 1:09 / 2:09 | 2:12 |
| 10 | — / — | — | 0:07 | 0:51 / 1:24 | 4:41 |
| 11 | — / — | — | 0:06 | 1:09 / 2:12 | 2:30 |
| 12 | — / — | — | 0:08 | 0:54 / 1:33 | 4:29 |
| 13 | — / — | — | 0:07 | 0:57 / 1:27 | 4:38 |
| 14 | — / — | — | 0:08 | 1:12 / 2:03 | 3:54 |
| 15 | — / — | — | 0:10 | 0:57 / 1:24 | 4:33 |
| 16 | — / — | — | 0:09 | 0:57 / 1:39 | 4:15 |
| 17 | — / — | — | 3:12 | 0:57 / 1:33 | 3:52 |
| 18 | — / — | — | 0:08 | 0:45 / 1:04 | 4:00 |
| 19 | — / — | — | 0:06 | 0:45 / 1:09 | 3:58 |
| 20 | — / — | — | 0:10 | 1:00 / 1:27 | 3:49 |
| 21 | — / — | — | 0:11 | 0:42 / 1:04 | 3:52 |
| 22 | — / — | — | 0:08 | 0:42 / 1:00 | 3:59 |
| 23 | — / — | — | 0:06 | 0:33 / 0:54 | 3:53 |
| 24 | — / — | — | 0:10 | 0:45 / 1:19 | 3:46 |
| 25 | — / — | — | 0:06 | 0:21 / bonus | 1:52 |

## 2025

You didn't play 2025, so there's nothing to compare. Claude's 2025 runs (days 1–12,
all 24 stars, no wrong answers) are in `2025-claude/`.

## Takeaways

- Claude earned all 100 stars across 2023 and 2024 with **no wrong answers**,
  including the parts you hadn't finished (2023 days 7, 12, 17–25 and 2024 days 5–25).
- On recognised puzzles the code is written within seconds. Waiting on the shared
  submit queue and the site's cooldown was most of each day's elapsed time.
- The live 2026 runs are the real benchmark: one unseen puzzle at a time, timed
  from unlock. Your closest comparable hand-solved times are 2023 days 9 and 11
  (about 3 hours from unlock) and the commit-gap estimates above.
