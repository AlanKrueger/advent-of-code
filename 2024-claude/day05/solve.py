import sys
from functools import cmp_to_key

text = open(sys.argv[1] if len(sys.argv) > 1 else "input").read()
rules_s, updates_s = text.strip().split("\n\n")
rules = {tuple(map(int, l.split("|"))) for l in rules_s.splitlines()}
updates = [list(map(int, l.split(","))) for l in updates_s.splitlines()]

def cmp(a, b):
    if (a, b) in rules:
        return -1
    if (b, a) in rules:
        return 1
    return 0

p1 = p2 = 0
for u in updates:
    s = sorted(u, key=cmp_to_key(cmp))
    if s == u:
        p1 += u[len(u) // 2]
    else:
        p2 += s[len(s) // 2]
print(f"part1: {p1}")
print(f"part2: {p2}")
