import sys

def find(g, smudges):
    n = len(g)
    for k in range(1, n):
        d = sum(a != b for i in range(min(k, n - k)) for a, b in zip(g[k - 1 - i], g[k + i]))
        if d == smudges:
            return k
    return 0

def score(g, s):
    return 100 * find(g, s) or find([''.join(c) for c in zip(*g)], s)

path = sys.argv[1] if len(sys.argv) > 1 else 'input'
pats = [p.split() for p in open(path).read().strip().split('\n\n')]
print('part1:', sum(score(p, 0) for p in pats))
print('part2:', sum(score(p, 1) for p in pats))
