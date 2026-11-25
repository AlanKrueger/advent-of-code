import sys
from functools import lru_cache

path = sys.argv[1] if len(sys.argv) > 1 else "input"
g = {}
for line in open(path).read().strip().splitlines():
    a, b = line.split(":")
    g[a.strip()] = b.split()


def count(src, dst):
    @lru_cache(None)
    def f(n):
        if n == dst:
            return 1
        return sum(f(m) for m in g.get(n, []))
    return f(src)


if "you" in g:
    print("part1:", count("you", "out"))

if "svr" in g:
    a = count("svr", "dac") * count("dac", "fft") * count("fft", "out")
    b = count("svr", "fft") * count("fft", "dac") * count("dac", "out")
    print("part2:", a + b)
