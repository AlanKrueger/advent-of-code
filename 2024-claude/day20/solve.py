import sys
from collections import Counter, deque

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "input"
    thr = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    hist = len(sys.argv) > 3
    g = open(path).read().split()
    for r, row in enumerate(g):
        for c, ch in enumerate(row):
            if ch == "S": s = (r, c)
    dist = {s: 0}
    q = deque([s])
    while q:
        r, c = q.popleft()
        for nr, nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
            if g[nr][nc] != "#" and (nr, nc) not in dist:
                dist[(nr, nc)] = dist[(r, c)] + 1
                q.append((nr, nc))
    for part, rad in ((1, 2), (2, 20)):
        cnt = Counter()
        for (r, c), d in dist.items():
            for dr in range(-rad, rad+1):
                rem = rad - abs(dr)
                for dc in range(-rem, rem+1):
                    e = dist.get((r+dr, c+dc))
                    if e is not None:
                        save = e - d - abs(dr) - abs(dc)
                        if save > 0: cnt[save] += 1
        if hist: print(part, sorted((k, v) for k, v in cnt.items() if k >= thr))
        print(f"part{part}: {sum(v for k, v in cnt.items() if k >= thr)}")

main()
