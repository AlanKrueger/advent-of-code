import sys
from math import prod

lines = open(sys.argv[1] if len(sys.argv) > 1 else "input").read().split("\n")
lines = [l for l in lines if l.strip()]
w = max(map(len, lines))
lines = [l.ljust(w) for l in lines]
rows, ops = lines[:-1], lines[-1]

# split into problems at all-space columns
blocks, cur = [], []
for c in range(w):
    if all(l[c] == " " for l in lines):
        if cur: blocks.append(cur); cur = []
    else:
        cur.append(c)
if cur: blocks.append(cur)

p1 = p2 = 0
for cols in blocks:
    op = ops[cols[0]:cols[-1] + 1].strip()
    f = sum if op == "+" else prod
    p1 += f(int(r[cols[0]:cols[-1] + 1]) for r in rows)
    p2 += f(int("".join(r[c] for r in rows)) for c in cols)
print(f"part1: {p1}")
print(f"part2: {p2}")
