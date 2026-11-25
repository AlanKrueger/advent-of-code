import sys


def parse(text):
    shapes, regions = [], []
    for block in text.strip().split("\n\n"):
        lines = block.splitlines()
        if "x" in lines[0]:
            for ln in lines:
                size, counts = ln.split(":")
                w, h = map(int, size.split("x"))
                regions.append((w, h, list(map(int, counts.split()))))
        else:
            shapes.append({(r, c) for r, row in enumerate(lines[1:]) for c, ch in enumerate(row) if ch == "#"})
    return shapes, regions


def orientations(shape):
    out = set()
    pts = shape
    for _ in range(2):
        for _ in range(4):
            pts = {(c, -r) for r, c in pts}
            mr = min(r for r, _ in pts); mc = min(c for _, c in pts)
            out.add(frozenset((r - mr, c - mc) for r, c in pts))
        pts = {(r, -c) for r, c in pts}
    return list(out)


def can_fit(w, h, counts, shapes, orients):
    if sum(n * len(shapes[i]) for i, n in enumerate(counts)) > w * h:
        return False
    if sum(counts) <= (w // 3) * (h // 3):
        return True
    # Exact search: take the first undecided cell; cover it with a remaining piece
    # (anchored at the piece's first row-major cell) or leave it empty if slack allows.
    left = list(counts)
    anchored = [[(o, min(o)) for o in os] for os in orients]
    grid = [False] * (w * h)
    slack = w * h - sum(n * len(shapes[i]) for i, n in enumerate(counts))

    def rec(pos):
        nonlocal slack
        if not any(left):
            return True
        while pos < w * h and grid[pos]:
            pos += 1
        if pos == w * h:
            return False
        r0, c0 = divmod(pos, w)
        for i in range(len(left)):
            if not left[i]:
                continue
            for o, (ar, ac) in anchored[i]:
                cells = []
                for r, c in o:
                    rr, cc = r0 + r - ar, c0 + c - ac
                    if not (0 <= rr < h and 0 <= cc < w) or grid[rr * w + cc]:
                        break
                    cells.append(rr * w + cc)
                else:
                    for p in cells:
                        grid[p] = True
                    left[i] -= 1
                    ok = rec(pos + 1)
                    left[i] += 1
                    for p in cells:
                        grid[p] = False
                    if ok:
                        return True
        if slack > 0:
            slack -= 1
            grid[pos] = True
            ok = rec(pos + 1)
            grid[pos] = False
            slack += 1
            return ok
        return False

    return rec(0)


def main():
    shapes, regions = parse(open(sys.argv[1] if len(sys.argv) > 1 else "input").read())
    orients = [orientations(s) for s in shapes]
    print("part1:", sum(can_fit(w, h, cnt, shapes, orients) for w, h, cnt in regions))


main()
