import sys

def counts(grid, targets):
    n, m = len(grid), len(grid[0])
    s = next((r, c) for r in range(n) for c in range(m) if grid[r][c] == 'S')
    seen = {s: 0}
    frontier = [s]
    out = {}
    mx = max(targets)
    d = 0
    while True:
        if d in targets:
            out[d] = sum(1 for v in seen.values() if v <= d and v % 2 == d % 2)
        if d == mx:
            return out
        d += 1
        nf = []
        for r, c in frontier:
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if (nr, nc) not in seen and grid[nr % n][nc % m] != '#':
                    seen[(nr, nc)] = d
                    nf.append((nr, nc))
        frontier = nf

def main():
    f = sys.argv[1] if len(sys.argv) > 1 else 'input'
    steps = int(sys.argv[2]) if len(sys.argv) > 2 else 64
    grid = open(f).read().split()
    print('part1:', counts(grid, {steps})[steps])
    if len(sys.argv) > 3:  # direct infinite-grid count (for example checks)
        t = int(sys.argv[3])
        print('part2:', counts(grid, {t})[t])
        return
    T = 26501365
    n = len(grid)
    r = T % n
    xs = [r, r + n, r + 2 * n]
    c = counts(grid, set(xs))
    y0, y1, y2 = (c[x] for x in xs)
    k = T // n
    # Newton forward differences
    a = y0; b = y1 - y0; cc = y2 - 2 * y1 + y0
    print('part2:', a + b * k + cc * k * (k - 1) // 2)

main()
