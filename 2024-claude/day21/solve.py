import sys
from functools import lru_cache
from itertools import permutations

NUM = {c: (r, k) for r, row in enumerate(["789", "456", "123", " 0A"]) for k, c in enumerate(row) if c != " "}
DIR = {c: (r, k) for r, row in enumerate([" ^A", "<v>"]) for k, c in enumerate(row) if c != " "}
MOVES = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def paths(pad, a, b):
    (r1, c1), (r2, c2) = pad[a], pad[b]
    ms = ("v" if r2 > r1 else "^") * abs(r2 - r1) + (">" if c2 > c1 else "<") * abs(c2 - c1)
    valid = set(pad.values())
    out = set()
    for p in set(permutations(ms)):
        r, c = r1, c1
        ok = True
        for m in p:
            r, c = r + MOVES[m][0], c + MOVES[m][1]
            if (r, c) not in valid:
                ok = False
                break
        if ok:
            out.add("".join(p) + "A")
    return out


@lru_cache(None)
def cost(seq, depth):
    # presses at the human keypad to type seq on a directional keypad 'depth' levels above
    if depth == 0:
        return len(seq)
    total, cur = 0, "A"
    for ch in seq:
        total += min(cost(p, depth - 1) for p in paths(DIR, cur, ch))
        cur = ch
    return total


def solve(code, robots):
    total, cur = 0, "A"
    for ch in code:
        total += min(cost(p, robots) for p in paths(NUM, cur, ch))
        cur = ch
    return total


f = sys.argv[1] if len(sys.argv) > 1 else "input"
codes = open(f).read().split()
for part, n in (("part1", 2), ("part2", 25)):
    print(f"{part}: {sum(solve(c, n) * int(c[:-1]) for c in codes)}")
