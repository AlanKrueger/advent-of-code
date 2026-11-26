# 2024 Day 17: Chronospatial Computer

Mode: practice · clock started 2026-11-26T00:06:23+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `2,1,4,0,7,4,0,2,3` | 0:02:54 | 117s | 0 |
| 2 | `258394985014171` | 0:05:25 | 115s | 0 |

## Approach
Part 1: Direct interpreter for the 8-opcode 3-bit machine.
Part 2: The program loops, shifting A right by 3 each pass and outputting one digit, so A is built
3 bits at a time from the last output digit backwards, keeping every candidate whose run reproduces
the program's suffix; answer is the smallest positive survivor.

## Log
- Recognised this puzzle from training data (the quine search in part 2), so part 2 was drafted
  before it unlocked and only submitted after matching the part 2 example (117440).
- First draft returned min including 0; added a positive filter after reading "lowest positive".
- Both parts correct first try. Most wall time was the shared submit queue/cooldown (~2 min each).
