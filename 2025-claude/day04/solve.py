import sys

def load(path):
    lines = open(path).read().split()
    return {(r, c) for r, line in enumerate(lines) for c, ch in enumerate(line) if ch == '@'}

def accessible(rolls):
    return {p for p in rolls
            if sum((p[0] + dr, p[1] + dc) in rolls
                   for dr in (-1, 0, 1) for dc in (-1, 0, 1) if dr or dc) < 4}

def main():
    rolls = load(sys.argv[1] if len(sys.argv) > 1 else 'input')
    print(f"part1: {len(accessible(rolls))}")
    start = len(rolls)
    while (gone := accessible(rolls)):
        rolls -= gone
    print(f"part2: {start - len(rolls)}")

main()
