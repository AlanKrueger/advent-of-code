import re, sys

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "input"
    limit = {"red": 12, "green": 13, "blue": 14}
    p1 = p2 = 0
    for line in open(path).read().splitlines():
        if not line.strip():
            continue
        gid = int(re.match(r"Game (\d+)", line).group(1))
        mx = {"red": 0, "green": 0, "blue": 0}
        for n, c in re.findall(r"(\d+) (red|green|blue)", line):
            mx[c] = max(mx[c], int(n))
        if all(mx[c] <= limit[c] for c in limit):
            p1 += gid
        p2 += mx["red"] * mx["green"] * mx["blue"]
    print(f"part1: {p1}")
    print(f"part2: {p2}")

main()
