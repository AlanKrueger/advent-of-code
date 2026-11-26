import sys


def total(gal, f):
    s = 0
    for axis in (0, 1):
        vals = sorted(g[axis] for g in gal)
        occ = set(vals)
        # map coordinate to expanded coordinate
        lo, hi = vals[0], vals[-1]
        pos, cur = {}, 0
        for c in range(lo, hi + 1):
            if c not in occ:
                cur += f - 1
            pos[c] = c + cur
        xs = sorted(pos[v] for v in vals)
        acc = 0
        for i, x in enumerate(xs):
            s += x * i - acc
            acc += x
    return s


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "input"
    f2 = int(sys.argv[2]) if len(sys.argv) > 2 else 1000000
    grid = open(path).read().split()
    gal = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "#"]
    print(f"part1: {total(gal, 2)}")
    print(f"part2: {total(gal, f2)}")


main()
