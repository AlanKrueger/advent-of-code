import sys
from itertools import combinations

path = sys.argv[1] if len(sys.argv) > 1 else "input"
pts = [tuple(map(int, l.split(","))) for l in open(path).read().split()]
n = len(pts)
k = 10 if n <= 20 else 1000
edges = sorted(
    (sum((a - b) ** 2 for a, b in zip(pts[i], pts[j])), i, j)
    for i, j in combinations(range(n), 2)
)
parent = list(range(n))
size = [1] * n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]
    return True

for _, i, j in edges[:k]:
    union(i, j)
s = sorted((size[r] for r in range(n) if find(r) == r), reverse=True)
print(f"part1: {s[0] * s[1] * s[2]}")

comps = len(s)
for _, i, j in edges[k:]:
    if union(i, j):
        comps -= 1
        if comps == 1:
            print(f"part2: {pts[i][0] * pts[j][0]}")
            break
