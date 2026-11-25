import sys
from collections import defaultdict

g = open(sys.argv[1] if len(sys.argv) > 1 else "input").read().split("\n")
g = [r for r in g if r]
beams = {g[0].index("S"): 1}
splits = 0
for row in g[1:]:
    nb = defaultdict(int)
    for c, n in beams.items():
        if row[c] == "^":
            splits += 1
            for d in (c - 1, c + 1):
                if 0 <= d < len(row):
                    nb[d] += n
        else:
            nb[c] += n
    beams = nb
print("part1:", splits)
print("part2:", sum(beams.values()))
