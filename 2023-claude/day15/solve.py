import sys


def h(s):
    v = 0
    for c in s:
        v = (v + ord(c)) * 17 % 256
    return v


steps = open(sys.argv[1] if len(sys.argv) > 1 else "input").read().replace("\n", "").split(",")
print("part1:", sum(h(s) for s in steps))

boxes = [dict() for _ in range(256)]
for s in steps:
    if s.endswith("-"):
        boxes[h(s[:-1])].pop(s[:-1], None)
    else:
        lab, f = s.split("=")
        boxes[h(lab)][lab] = int(f)
print("part2:", sum((b + 1) * i * f for b, box in enumerate(boxes)
                    for i, f in enumerate(box.values(), 1)))
