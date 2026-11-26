import sys

def energize(g, start):
    H, W = len(g), len(g[0])
    seen = set()
    stack = [start]
    while stack:
        r, c, dr, dc = stack.pop()
        if not (0 <= r < H and 0 <= c < W) or (r, c, dr, dc) in seen:
            continue
        seen.add((r, c, dr, dc))
        ch = g[r][c]
        if ch == '/':
            dirs = [(-dc, -dr)]
        elif ch == '\\':
            dirs = [(dc, dr)]
        elif ch == '|' and dc:
            dirs = [(-1, 0), (1, 0)]
        elif ch == '-' and dr:
            dirs = [(0, -1), (0, 1)]
        else:
            dirs = [(dr, dc)]
        for nr, nc in dirs:
            stack.append((r + nr, c + nc, nr, nc))
    return len({(r, c) for r, c, _, _ in seen})

def main():
    f = sys.argv[1] if len(sys.argv) > 1 else 'input'
    g = open(f).read().split()
    H, W = len(g), len(g[0])
    print('part1:', energize(g, (0, 0, 0, 1)))
    starts = [(r, 0, 0, 1) for r in range(H)] + [(r, W-1, 0, -1) for r in range(H)]
    starts += [(0, c, 1, 0) for c in range(W)] + [(H-1, c, -1, 0) for c in range(W)]
    print('part2:', max(energize(g, s) for s in starts))

main()
