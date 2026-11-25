import sys, re
from itertools import combinations

def parse(path):
    ms = []
    for line in open(path).read().split('\n'):
        if not line.strip():
            continue
        lights = re.search(r'\[([.#]+)\]', line).group(1)
        buttons = [tuple(map(int, b.split(','))) for b in re.findall(r'\(([\d,]+)\)', line)]
        jolt = list(map(int, re.search(r'\{([\d,]+)\}', line).group(1).split(',')))
        ms.append((lights, buttons, jolt))
    return ms

def part1(ms):
    total = 0
    for lights, buttons, _ in ms:
        target = sum(1 << i for i, c in enumerate(lights) if c == '#')
        masks = [sum(1 << i for i in b) for b in buttons]
        done = False
        for k in range(len(masks) + 1):
            for combo in combinations(masks, k):
                x = 0
                for m in combo:
                    x ^= m
                if x == target:
                    total += k
                    done = True
                    break
            if done:
                break
    return total

from functools import lru_cache

def min_jolt(buttons, jolt):
    n = len(jolt)
    # every subset of buttons pressed once: (parity pattern) -> list of (effect vector, count)
    by_parity = {}
    nb = len(buttons)
    for mask in range(1 << nb):
        eff = [0] * n
        cnt = 0
        for j in range(nb):
            if mask >> j & 1:
                cnt += 1
                for i in buttons[j]:
                    eff[i] += 1
        par = tuple(e & 1 for e in eff)
        by_parity.setdefault(par, []).append((tuple(eff), cnt))
    INF = float('inf')

    @lru_cache(maxsize=None)
    def f(b):
        if not any(b):
            return 0
        best = INF
        for eff, cnt in by_parity.get(tuple(x & 1 for x in b), ()):
            if all(e <= x for e, x in zip(eff, b)):
                r = f(tuple((x - e) // 2 for x, e in zip(b, eff)))
                if cnt + 2 * r < best:
                    best = cnt + 2 * r
        return best

    return f(tuple(jolt))

def part2(ms):
    return sum(min_jolt(b, j) for _, b, j in ms)

ms = parse(sys.argv[1] if len(sys.argv) > 1 else 'input')
print('part1:', part1(ms))
print('part2:', part2(ms))
