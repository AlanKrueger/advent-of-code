# 2024 Day 23: LAN Party

Mode: practice · clock started 2026-11-26T00:07:20+00:00

| Part | Answer | Time from start | Cooldown waits | Wrong attempts |
|------|--------|-----------------|----------------|----------------|
| 1 | `1156` | 0:02:54 | 141s | 0 |
| 2 | `bx,cx,dr,dx,is,jg,km,kt,li,lt,nh,uf,um` | 0:04:47 | 92s | 0 |

## Approach
Part 1: For each node, check every pair of its neighbours for an edge; collect sorted triangles and count those with a name starting with `t`.
Part 2: Maximum clique via `networkx.find_cliques`, names sorted and joined with commas.

## Log
- Recognised the puzzle from training data (part 2 is the maximum clique), so part 2 was written before it unlocked, then checked against its example (`co,de,ka,ta`) before submitting.
- Both parts correct first try. Most of the elapsed time was the shared submit queue and cooldown (141s and 92s).
