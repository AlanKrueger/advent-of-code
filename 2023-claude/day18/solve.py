import sys

D = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1)}


def area(steps):
    x = y = 0
    a2 = perim = 0
    for d, n in steps:
        dx, dy = D[d]
        nx, ny = x + dx * n, y + dy * n
        a2 += x * ny - nx * y
        perim += n
        x, y = nx, ny
    # Pick's theorem: interior + boundary
    return abs(a2) // 2 + perim // 2 + 1


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'input'
    lines = open(path).read().split('\n')
    p1, p2 = [], []
    for line in lines:
        if not line.strip():
            continue
        d, n, c = line.split()
        p1.append((d, int(n)))
        h = c.strip('(#)')
        p2.append(('RDLU'[int(h[5])], int(h[:5], 16)))
    print(f'part1: {area(p1)}')
    print(f'part2: {area(p2)}')


main()
