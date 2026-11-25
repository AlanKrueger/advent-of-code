import sys

lines = open(sys.argv[1] if len(sys.argv) > 1 else "input").read().split()
moves = [(-1 if s[0] == "L" else 1, int(s[1:])) for s in lines]

pos, p1 = 50, 0
for d, n in moves:
    pos = (pos + d * n) % 100
    p1 += pos == 0
print("part1:", p1)

# Part 2: count every click that lands on 0. Inputs are small, so step click by click.
pos, p2 = 50, 0
for d, n in moves:
    for _ in range(n):
        pos = (pos + d) % 100
        p2 += pos == 0
print("part2:", p2)
