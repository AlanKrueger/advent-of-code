import sys


def tilt_north(g):
    g = [list(r) for r in g]
    H, W = len(g), len(g[0])
    for c in range(W):
        top = 0
        for r in range(H):
            if g[r][c] == '#':
                top = r + 1
            elif g[r][c] == 'O':
                g[r][c] = '.'
                g[top][c] = 'O'
                top += 1
    return [''.join(r) for r in g]


def rot_cw(g):
    return [''.join(g[len(g) - 1 - r][c] for r in range(len(g))) for c in range(len(g[0]))]


def load(g):
    H = len(g)
    return sum((H - r) * row.count('O') for r, row in enumerate(g))


def cycle(g):
    for _ in range(4):  # N, W, S, E: tilt north then rotate clockwise
        g = rot_cw(tilt_north(g))
    return g


def main():
    f = sys.argv[1] if len(sys.argv) > 1 else 'input'
    g = open(f).read().split()
    print('part1:', load(tilt_north(g)))
    N = 1000000000
    seen, hist = {}, []
    t = tuple(g)
    i = 0
    while t not in seen:
        seen[t] = i
        hist.append(t)
        t = tuple(cycle(list(t)))
        i += 1
    s = seen[t]
    print('part2:', load(hist[s + (N - s) % (i - s)]))


main()
