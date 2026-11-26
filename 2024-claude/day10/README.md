# 2024 Day 10: Hoof It

Mode: practice · clock started 2026-11-26T00:05:08+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `593` | 0:03:21 | 150s | 0 |
| 2 | `1192` | 0:06:05 | 131s | 0 |

## Approach
Part 1: Memoized DFS from each 0 along +1 steps, collecting the set of reachable 9s; sum the set sizes.
Part 2: Same DFS, memoized count of distinct paths to any 9 instead of the set.

## Log
- Recognised the puzzle from training data (part 2 is distinct-path count), so both parts were written before part 2 unlocked; part 2 was submitted only after its text and example (81) were checked.
- Both examples matched first try; no wrong answers. Most elapsed time was queue/cooldown waiting behind other runs' submits.
