import sys


def nxt(s):
    if not any(s):
        return 0
    return s[-1] + nxt([b - a for a, b in zip(s, s[1:])])


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "input"
    rows = [list(map(int, l.split())) for l in open(path) if l.strip()]
    print(f"part1: {sum(nxt(r) for r in rows)}")
    print(f"part2: {sum(nxt(r[::-1]) for r in rows)}")


if __name__ == "__main__":
    main()
