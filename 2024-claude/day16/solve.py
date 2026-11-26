import sys, heapq

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # E S W N


def dijkstra(g, starts):
    dist = {}
    pq = [(0, s) for s in starts]
    heapq.heapify(pq)
    while pq:
        d, st = heapq.heappop(pq)
        if st in dist:
            continue
        dist[st] = d
        yield st, d
        r, c, k = st
        nb = [(d + 1000, (r, c, (k + 1) % 4)), (d + 1000, (r, c, (k - 1) % 4))]
        dr, dc = DIRS[k]
        if g[r + dr][c + dc] != '#':
            nb.append((d + 1, (r + dr, c + dc, k)))
        for nd, ns in nb:
            if ns not in dist:
                heapq.heappush(pq, (nd, ns))


def main():
    f = sys.argv[1] if len(sys.argv) > 1 else 'input'
    g = open(f).read().split()
    for r, row in enumerate(g):
        for c, ch in enumerate(row):
            if ch == 'S':
                S = (r, c)
            elif ch == 'E':
                E = (r, c)
    fw = dict(dijkstra(g, [(S[0], S[1], 0)]))
    best = min(fw.get((E[0], E[1], k), float('inf')) for k in range(4))
    print('part1:', best)
    # backward search: reverse direction; state (r,c,k) moving with k reversed
    bw = dict(dijkstra(g, [(E[0], E[1], k) for k in range(4)]))
    tiles = set()
    for (r, c, k), d in fw.items():
        b = bw.get((r, c, (k + 2) % 4))
        if b is not None and d + b == best:
            tiles.add((r, c))
    print('part2:', len(tiles))


main()
