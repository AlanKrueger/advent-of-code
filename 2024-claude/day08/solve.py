import sys
from math import gcd
from itertools import combinations
from collections import defaultdict

grid = open(sys.argv[1] if len(sys.argv) > 1 else "input").read().split()
H, W = len(grid), len(grid[0])
ants = defaultdict(list)
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch != ".":
            ants[ch].append((r, c))
inb = lambda r, c: 0 <= r < H and 0 <= c < W
p1, p2 = set(), set()
for pts in ants.values():
    for (r1, c1), (r2, c2) in combinations(pts, 2):
        dr, dc = r2 - r1, c2 - c1
        for r, c in ((r1 - dr, c1 - dc), (r2 + dr, c2 + dc)):
            if inb(r, c):
                p1.add((r, c))
        g = gcd(dr, dc)
        sr, sc = dr // g, dc // g
        for s in (1, -1):
            r, c = r1, c1
            while inb(r, c):
                p2.add((r, c))
                r += s * sr; c += s * sc
print("part1:", len(p1))
print("part2:", len(p2))
