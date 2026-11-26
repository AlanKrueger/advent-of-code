import re, sys

f = sys.argv[1] if len(sys.argv) > 1 else "input"
W = int(sys.argv[2]) if len(sys.argv) > 2 else 101
H = int(sys.argv[3]) if len(sys.argv) > 3 else 103
R = [tuple(map(int, re.findall(r"-?\d+", l))) for l in open(f) if l.strip()]

def at(t):
    return [((x + vx * t) % W, (y + vy * t) % H) for x, y, vx, vy in R]

def safety(ps):
    q = [0] * 4
    for x, y in ps:
        if x == W // 2 or y == H // 2:
            continue
        q[(x > W // 2) + 2 * (y > H // 2)] += 1
    return q[0] * q[1] * q[2] * q[3]

print("part1:", safety(at(100)))
if (W, H) == (101, 103):
    # The tree picture: first time step where no two robots share a tile.
    for t in range(W * H):
        ps = at(t)
        if len(set(ps)) == len(ps):
            break
    s = set(ps)
    if "-v" in sys.argv:
        for y in range(H):
            print("".join("#" if (x, y) in s else "." for x in range(W)))
    print("part2:", t)
