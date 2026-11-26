import sys
from math import isqrt, prod


def ways(t, d):
    # count h in [0, t] with h*(t-h) > d
    r = isqrt(t * t - 4 * d) if t * t > 4 * d else 0
    lo = max(0, (t - r) // 2 - 2)
    while lo * (t - lo) <= d:
        lo += 1
    hi = t - lo
    return max(0, hi - lo + 1)


def main():
    lines = open(sys.argv[1] if len(sys.argv) > 1 else "input").read().splitlines()
    rows = [l.split(":")[1].split() for l in lines[:2]]
    print("part1:", prod(ways(int(t), int(d)) for t, d in zip(*rows)))
    print("part2:", ways(int("".join(rows[0])), int("".join(rows[1]))))


main()
