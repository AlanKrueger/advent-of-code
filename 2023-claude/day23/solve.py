import sys
sys.setrecursionlimit(10000)
g = open(sys.argv[1] if len(sys.argv) > 1 else 'input').read().split()
H, W = len(g), len(g[0])
start = (0, g[0].index('.')); end = (H - 1, g[-1].index('.'))
D = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def nbrs(r, c, slopes):
    ch = g[r][c]
    dirs = [D[ch]] if slopes and ch in D else D.values()
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < H and 0 <= nc < W and g[nr][nc] != '#':
            yield nr, nc

def solve(slopes):
    nodes = [start, end] + [(r, c) for r in range(H) for c in range(W) if g[r][c] != '#'
                            and sum(1 for _ in nbrs(r, c, False)) >= 3]
    idx = {n: i for i, n in enumerate(nodes)}
    adj = [[] for _ in nodes]
    for n in nodes:
        for s in nbrs(*n, slopes):
            prev, cur, d = n, s, 1
            ok = True
            while cur not in idx:
                nx = [x for x in nbrs(*cur, slopes) if x != prev]
                if not nx: ok = False; break
                prev, cur, d = cur, nx[0], d + 1
            if ok: adj[idx[n]].append((idx[cur], d))
    # if end has single neighbor, reaching it means must go to end
    tgt, extra = 1, 0
    into = [(i, d) for i in range(len(nodes)) for j, d in adj[i] if j == 1]
    if len(into) == 1: tgt, extra = into[0]
    best = -1
    def dfs(u, seen, dist):
        nonlocal best
        if u == tgt:
            if dist > best: best = dist
            return
        for v, d in adj[u]:
            b = 1 << v
            if not seen & b: dfs(v, seen | b, dist + d)
    dfs(0, 1, 0)
    return best + extra

print('part1:', solve(True))
print('part2:', solve(False))
