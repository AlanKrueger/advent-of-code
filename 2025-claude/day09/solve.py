import sys
from collections import deque

pts = [tuple(map(int, l.split(","))) for l in open(sys.argv[1] if len(sys.argv) > 1 else "input").read().split()]
n = len(pts)

def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

print("part1:", max(area(pts[i], pts[j]) for i in range(n) for j in range(i + 1, n)))

# Part 2: compress coordinates; each distinct value is a cell, gaps between are cells too.
xs = sorted({p[0] for p in pts}); ys = sorted({p[1] for p in pts})
xi = {x: 2 * i + 1 for i, x in enumerate(xs)}; yi = {y: 2 * i + 1 for i, y in enumerate(ys)}
W = 2 * len(xs) + 1; H = 2 * len(ys) + 1
grid = [[0] * W for _ in range(H)]  # 1 = boundary
for k in range(n):
    (x1, y1), (x2, y2) = pts[k], pts[(k + 1) % n]
    a, b = sorted((xi[x1], xi[x2])); c, d = sorted((yi[y1], yi[y2]))
    for yy in range(c, d + 1):
        for xx in range(a, b + 1):
            grid[yy][xx] = 1
outside = [[False] * W for _ in range(H)]
q = deque([(0, 0)]); outside[0][0] = True
while q:
    x, y = q.popleft()
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H and not outside[ny][nx] and not grid[ny][nx]:
            outside[ny][nx] = True; q.append((nx, ny))
P = [[0] * (W + 1) for _ in range(H + 1)]
for y in range(H):
    for x in range(W):
        P[y + 1][x + 1] = P[y][x + 1] + P[y + 1][x] - P[y][x] + outside[y][x]
best = 0
for i in range(n):
    for j in range(i + 1, n):
        ar = area(pts[i], pts[j])
        if ar <= best:
            continue
        a, b = sorted((xi[pts[i][0]], xi[pts[j][0]])); c, d = sorted((yi[pts[i][1]], yi[pts[j][1]]))
        if P[d + 1][b + 1] - P[c][b + 1] - P[d + 1][a] + P[c][a] == 0:
            best = ar
print("part2:", best)
