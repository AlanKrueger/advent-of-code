import sys

D = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}


def run(grid, moves, box):
    g = {(r, c): ch for r, row in enumerate(grid) for c, ch in enumerate(row)}
    pos = next(p for p, ch in g.items() if ch == '@')
    for m in moves:
        dr, dc = D[m]
        # BFS collect cells to push
        front = [pos]
        tomove = []
        seen = set()
        ok = True
        while front:
            nf = []
            for p in front:
                if p in seen:
                    continue
                seen.add(p)
                tomove.append(p)
                q = (p[0] + dr, p[1] + dc)
                ch = g[q]
                if ch == '#':
                    ok = False
                    break
                if ch in 'O[]':
                    nf.append(q)
                    if dr and ch == '[':
                        nf.append((q[0], q[1] + 1))
                    if dr and ch == ']':
                        nf.append((q[0], q[1] - 1))
            if not ok:
                break
            front = nf
        if not ok:
            continue
        vals = {p: g[p] for p in tomove}
        for p in tomove:
            g[p] = '.'
        for p in tomove:
            g[(p[0] + dr, p[1] + dc)] = vals[p]
        pos = (pos[0] + dr, pos[1] + dc)
    return sum(100 * r + c for (r, c), ch in g.items() if ch == box)


def main():
    f = sys.argv[1] if len(sys.argv) > 1 else 'input'
    a, b = open(f).read().split('\n\n')
    grid = a.split('\n')
    moves = ''.join(b.split())
    print('part1:', run(grid, moves, 'O'))
    wide = [''.join({'#': '##', 'O': '[]', '.': '..', '@': '@.'}[ch] for ch in row) for row in grid]
    print('part2:', run(wide, moves, '['))


main()
