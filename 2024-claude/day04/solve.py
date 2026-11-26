import sys

g = open(sys.argv[1] if len(sys.argv) > 1 else 'input').read().split()
H, W = len(g), len(g[0])

def at(r, c):
    return g[r][c] if 0 <= r < H and 0 <= c < W else ''

p1 = sum(all(at(r + dr * i, c + dc * i) == ch for i, ch in enumerate('XMAS'))
         for r in range(H) for c in range(W)
         for dr in (-1, 0, 1) for dc in (-1, 0, 1) if dr or dc)
p2 = sum(g[r][c] == 'A'
         and {at(r - 1, c - 1), at(r + 1, c + 1)} == {'M', 'S'}
         and {at(r - 1, c + 1), at(r + 1, c - 1)} == {'M', 'S'}
         for r in range(H) for c in range(W))
print(f'part1: {p1}')
print(f'part2: {p2}')
