import sys

path = sys.argv[1] if len(sys.argv) > 1 else "input"
top, bottom = open(path).read().strip().split("\n\n")
ranges = [tuple(map(int, l.split("-"))) for l in top.split()]
ids = [int(x) for x in bottom.split()]

print("part1:", sum(any(a <= i <= b for a, b in ranges) for i in ids))

merged = []
for a, b in sorted(ranges):
    if merged and a <= merged[-1][1] + 1:
        merged[-1][1] = max(merged[-1][1], b)
    else:
        merged.append([a, b])
print("part2:", sum(b - a + 1 for a, b in merged))
