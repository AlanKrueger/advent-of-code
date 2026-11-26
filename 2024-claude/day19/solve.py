import sys
from functools import lru_cache

f = sys.argv[1] if len(sys.argv) > 1 else "input"
top, bottom = open(f).read().split("\n\n")
pats = set(p.strip() for p in top.split(","))
maxlen = max(map(len, pats))
designs = bottom.split()

def ways(d):
    n = len(d)
    dp = [0] * (n + 1)
    dp[n] = 1
    for i in range(n - 1, -1, -1):
        dp[i] = sum(dp[i + k] for k in range(1, min(maxlen, n - i) + 1) if d[i:i + k] in pats)
    return dp[0]

w = [ways(d) for d in designs]
print("part1:", sum(1 for x in w if x))
print("part2:", sum(w))
