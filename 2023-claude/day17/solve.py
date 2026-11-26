import sys, heapq

def solve(g, lo, hi):
    R, C = len(g), len(g[0])
    best = {}
    pq = [(0, 0, 0, 0), (0, 0, 0, 1)]  # cost, r, c, axis (0 = next move horizontal, 1 = vertical)
    while pq:
        d, r, c, ax = heapq.heappop(pq)
        if (r, c) == (R - 1, C - 1):
            return d
        if best.get((r, c, ax), 1 << 60) < d:
            continue
        for s in (1, -1):
            nd, nr, nc = d, r, c
            for k in range(1, hi + 1):
                if ax == 0: nc += s
                else: nr += s
                if not (0 <= nr < R and 0 <= nc < C): break
                nd += g[nr][nc]
                if k >= lo:
                    key = (nr, nc, 1 - ax)
                    if nd < best.get(key, 1 << 60):
                        best[key] = nd
                        heapq.heappush(pq, (nd, nr, nc, 1 - ax))

g = [list(map(int, l)) for l in open(sys.argv[1] if len(sys.argv) > 1 else 'input').read().split()]
print('part1:', solve(g, 1, 3))
print('part2:', solve(g, 4, 10))
