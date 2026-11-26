import sys
from functools import lru_cache

g = [l for l in open(sys.argv[1] if len(sys.argv) > 1 else 'input').read().split('\n') if l]
H, W = len(g), len(g[0])

def h(r, c):
    ch = g[r][c]
    return int(ch) if ch.isdigit() else -1

def nbrs(r, c):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < H and 0 <= nc < W and h(nr, nc) == h(r, c) + 1:
            yield nr, nc

@lru_cache(None)
def ends(r, c):
    if h(r, c) == 9:
        return frozenset([(r, c)])
    s = frozenset()
    for n in nbrs(r, c):
        s |= ends(*n)
    return s

@lru_cache(None)
def paths(r, c):
    if h(r, c) == 9:
        return 1
    return sum(paths(*n) for n in nbrs(r, c))

heads = [(r, c) for r in range(H) for c in range(W) if h(r, c) == 0]
print('part1:', sum(len(ends(*p)) for p in heads))
print('part2:', sum(paths(*p) for p in heads))
