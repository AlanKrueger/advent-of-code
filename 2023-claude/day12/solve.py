import sys
from functools import lru_cache

def count(s, groups):
    s = s + '.'
    @lru_cache(None)
    def f(i, g):
        if g == len(groups):
            return 0 if '#' in s[i:] else 1
        if i >= len(s):
            return 0
        r = 0
        if s[i] in '.?':
            r += f(i + 1, g)
        n = groups[g]
        if s[i] in '#?' and i + n < len(s) and '.' not in s[i:i+n] and s[i+n] != '#':
            r += f(i + n + 1, g + 1)
        return r
    return f(0, 0)

lines = open(sys.argv[1] if len(sys.argv) > 1 else 'input').read().split('\n')
p1 = p2 = 0
for line in lines:
    if not line.strip(): continue
    s, g = line.split()
    g = tuple(map(int, g.split(',')))
    p1 += count(s, g)
    p2 += count('?'.join([s]*5), g*5)
print(f"part1: {p1}")
print(f"part2: {p2}")
