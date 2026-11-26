import re, sys
s = open(sys.argv[1] if len(sys.argv) > 1 else "input").read()
p1 = p2 = 0
on = True
for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", s):
    t = m.group(0)
    if t == "do()": on = True
    elif t == "don't()": on = False
    else:
        v = int(m.group(1)) * int(m.group(2))
        p1 += v
        if on: p2 += v
print(f"part1: {p1}")
print(f"part2: {p2}")
