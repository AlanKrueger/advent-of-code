import sys
from collections import Counter

def blink(c):
    n = Counter()
    for v, k in c.items():
        if v == 0:
            n[1] += k
        else:
            s = str(v)
            if len(s) % 2 == 0:
                h = len(s) // 2
                n[int(s[:h])] += k
                n[int(s[h:])] += k
            else:
                n[v * 2024] += k
    return n

def run(c, times):
    for _ in range(times):
        c = blink(c)
    return sum(c.values())

f = sys.argv[1] if len(sys.argv) > 1 else "input"
c = Counter(int(x) for x in open(f).read().split())
print("part1:", run(c, 25))
print("part2:", run(c, 75))
