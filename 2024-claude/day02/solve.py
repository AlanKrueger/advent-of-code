import sys


def safe(r):
    d = [b - a for a, b in zip(r, r[1:])]
    return all(1 <= x <= 3 for x in d) or all(-3 <= x <= -1 for x in d)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "input"
    reports = [list(map(int, l.split())) for l in open(path) if l.strip()]
    print("part1:", sum(safe(r) for r in reports))
    print("part2:", sum(any(safe(r[:i] + r[i + 1:]) for i in range(len(r))) for r in reports))


main()
