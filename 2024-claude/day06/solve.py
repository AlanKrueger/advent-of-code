import sys

def main():
    fn = sys.argv[1] if len(sys.argv) > 1 else 'input'
    g = open(fn).read().split()
    H, W = len(g), len(g[0])
    walls = set()
    for r, row in enumerate(g):
        for c, ch in enumerate(row):
            if ch == '#': walls.add((r, c))
            elif ch == '^': start = (r, c)
    D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def walk(extra=None):
        r, c = start; d = 0
        seen = set(); states = set()
        while True:
            if (r, c, d) in states: return None
            states.add((r, c, d)); seen.add((r, c))
            nr, nc = r + D[d][0], c + D[d][1]
            if not (0 <= nr < H and 0 <= nc < W): return seen
            if (nr, nc) in walls or (nr, nc) == extra: d = (d + 1) % 4
            else: r, c = nr, nc

    path = walk()
    print(f"part1: {len(path)}")
    print(f"part2: {sum(walk(p) is None for p in path if p != start)}")

main()
