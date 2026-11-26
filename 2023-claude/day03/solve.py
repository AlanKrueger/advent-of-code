import sys, re
from collections import defaultdict

grid = open(sys.argv[1] if len(sys.argv) > 1 else "input").read().split("\n")
grid = [l for l in grid if l]
H = len(grid)
p1 = 0
gears = defaultdict(list)
for r, line in enumerate(grid):
    for m in re.finditer(r"\d+", line):
        n = int(m.group())
        part = False
        for rr in range(r - 1, r + 2):
            if not 0 <= rr < H:
                continue
            for cc in range(m.start() - 1, m.end() + 1):
                if 0 <= cc < len(grid[rr]):
                    ch = grid[rr][cc]
                    if ch != "." and not ch.isdigit():
                        part = True
                        if ch == "*":
                            gears[rr, cc].append(n)
        if part:
            p1 += n
print(f"part1: {p1}")
print(f"part2: {sum(v[0] * v[1] for v in gears.values() if len(v) == 2)}")
