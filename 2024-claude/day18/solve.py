import sys
from collections import deque

f = sys.argv[1] if len(sys.argv) > 1 else "input"
N = int(sys.argv[2]) if len(sys.argv) > 2 else 70
K = int(sys.argv[3]) if len(sys.argv) > 3 else 1024
pts = [tuple(map(int, l.split(","))) for l in open(f).read().split()]

def bfs(blocked):
    if (0, 0) in blocked:
        return None
    dist = {(0, 0): 0}
    q = deque([(0, 0)])
    while q:
        p = q.popleft()
        if p == (N, N):
            return dist[p]
        x, y = p
        for n in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= n[0] <= N and 0 <= n[1] <= N and n not in blocked and n not in dist:
                dist[n] = dist[p] + 1
                q.append(n)
    return None

print("part1:", bfs(set(pts[:K])))
lo, hi = 0, len(pts)  # find smallest k with no path using pts[:k]
while lo < hi:
    m = (lo + hi) // 2
    if bfs(set(pts[:m])) is None:
        hi = m
    else:
        lo = m + 1
print("part2: %d,%d" % pts[lo - 1])
