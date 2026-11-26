import re, sys

def cost(ax, ay, bx, by, px, py, limit=None):
    det = ax * by - ay * bx
    if det == 0:
        raise ValueError("degenerate machine")
    a, ra = divmod(px * by - py * bx, det)
    b, rb = divmod(ax * py - ay * px, det)
    if ra or rb or a < 0 or b < 0:
        return 0
    if limit is not None and (a > limit or b > limit):
        return 0
    return 3 * a + b

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "input"
    machines = [list(map(int, re.findall(r"\d+", blk))) for blk in open(path).read().split("\n\n") if blk.strip()]
    print("part1:", sum(cost(*m, limit=100) for m in machines))
    off = 10000000000000
    print("part2:", sum(cost(*m[:4], m[4] + off, m[5] + off) for m in machines))

main()
