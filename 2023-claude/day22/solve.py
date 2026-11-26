import sys
from collections import deque

def main():
    fn = sys.argv[1] if len(sys.argv) > 1 else 'input'
    bricks = []
    for line in open(fn).read().split():
        a, b = line.split('~')
        a = list(map(int, a.split(','))); b = list(map(int, b.split(',')))
        bricks.append((min(a[0],b[0]),min(a[1],b[1]),min(a[2],b[2]),max(a[0],b[0]),max(a[1],b[1]),max(a[2],b[2])))
    bricks.sort(key=lambda t: t[2])
    top = {}  # (x,y) -> (z, brick id)
    n = len(bricks)
    below = [set() for _ in range(n)]
    above = [set() for _ in range(n)]
    for i, (x1,y1,z1,x2,y2,z2) in enumerate(bricks):
        cells = [(x,y) for x in range(x1,x2+1) for y in range(y1,y2+1)]
        h = max((top[c][0] for c in cells if c in top), default=0)
        for c in cells:
            if c in top and top[c][0] == h:
                below[i].add(top[c][1]); above[top[c][1]].add(i)
        nz = h + 1 + (z2 - z1)
        for c in cells:
            top[c] = (nz, i)
    p1 = sum(all(len(below[j]) > 1 for j in above[i]) for i in range(n))
    print(f"part1: {p1}")
    p2 = 0
    for i in range(n):
        fallen = {i}; q = deque([i])
        while q:
            k = q.popleft()
            for j in above[k]:
                if j not in fallen and below[j] <= fallen:
                    fallen.add(j); q.append(j)
        p2 += len(fallen) - 1
    print(f"part2: {p2}")

main()
