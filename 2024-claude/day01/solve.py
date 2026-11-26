import sys
from collections import Counter

f = sys.argv[1] if len(sys.argv) > 1 else "input"
pairs = [tuple(map(int, l.split())) for l in open(f) if l.strip()]
a = sorted(p[0] for p in pairs)
b = sorted(p[1] for p in pairs)
print("part1:", sum(abs(x - y) for x, y in zip(a, b)))
c = Counter(b)
print("part2:", sum(x * c[x] for x in a))
