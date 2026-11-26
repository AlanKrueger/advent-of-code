import sys
from collections import defaultdict

M = 16777216


def step(s):
    s = ((s << 6) ^ s) % M
    s = ((s >> 5) ^ s) % M
    s = ((s << 11) ^ s) % M
    return s


def main():
    fn = sys.argv[1] if len(sys.argv) > 1 else "input"
    seeds = [int(x) for x in open(fn).read().split()]
    p1 = 0
    totals = defaultdict(int)
    for s in seeds:
        prices = [s % 10]
        for _ in range(2000):
            s = step(s)
            prices.append(s % 10)
        p1 += s
        seen = set()
        d = [prices[i + 1] - prices[i] for i in range(2000)]
        for i in range(3, 2000):
            k = (d[i - 3], d[i - 2], d[i - 1], d[i])
            if k not in seen:
                seen.add(k)
                totals[k] += prices[i + 1]
    print(f"part1: {p1}")
    print(f"part2: {max(totals.values())}")


main()
