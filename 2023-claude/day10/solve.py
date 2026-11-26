import sys

D = {'|': 'NS', '-': 'EW', 'L': 'NE', 'J': 'NW', '7': 'SW', 'F': 'SE'}
V = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
OPP = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

g = [list(l) for l in open(sys.argv[1] if len(sys.argv) > 1 else 'input').read().split('\n') if l]
H, W = len(g), len(g[0])
sr, sc = next((r, c) for r in range(H) for c in range(W) if g[r][c] == 'S')
sd = ''
for d in 'NSEW':
    r, c = sr + V[d][0], sc + V[d][1]
    if 0 <= r < H and 0 <= c < W and OPP[d] in D.get(g[r][c], ''):
        sd += d
g[sr][sc] = next(k for k, v in D.items() if set(v) == set(sd))

loop = {(sr, sc)}
r, c, d = sr, sc, sd[0]
while True:
    r, c = r + V[d][0], c + V[d][1]
    if (r, c) == (sr, sc):
        break
    loop.add((r, c))
    d = next(x for x in D[g[r][c]] if x != OPP[d])
print('part1:', len(loop) // 2)

inside = 0
for r in range(H):
    cross = False
    for c in range(W):
        if (r, c) in loop:
            if 'N' in D[g[r][c]]:
                cross = not cross
        elif cross:
            inside += 1
print('part2:', inside)
