import sys

W = "one two three four five six seven eight nine".split()


def digits(line, words):
    out = []
    for i, c in enumerate(line):
        if c.isdigit():
            out.append(int(c))
        elif words:
            for n, w in enumerate(W, 1):
                if line.startswith(w, i):
                    out.append(n)
    return out


def total(lines, words):
    s = 0
    for l in lines:
        d = digits(l, words)
        if d:
            s += d[0] * 10 + d[-1]
    return s


lines = open(sys.argv[1] if len(sys.argv) > 1 else "input").read().split()
print(f"part1: {total(lines, False)}")
print(f"part2: {total(lines, True)}")
