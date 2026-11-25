import sys


def best(bank, k):
    out, start = [], 0
    for remaining in range(k, 0, -1):
        end = len(bank) - remaining + 1
        d = max(bank[start:end])
        start = bank.index(d, start, end) + 1
        out.append(d)
    return int("".join(out))


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "input"
    banks = open(path).read().split()
    print(f"part1: {sum(best(b, 2) for b in banks)}")
    print(f"part2: {sum(best(b, 12) for b in banks)}")


main()
