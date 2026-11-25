import sys

text = open(sys.argv[1] if len(sys.argv) > 1 else "input").read()
ranges = [tuple(map(int, r.split("-"))) for r in text.replace("\n", "").split(",") if r.strip()]
maxlen = len(str(max(b for _, b in ranges)))


def candidates(part2):
    # Every number of the form p repeated r times (r == 2 for part 1, r >= 2 for part 2).
    out = set()
    for L in range(2, maxlen + 1):
        for k in range(1, L // 2 + 1):
            if L % k:
                continue
            r = L // k
            if not part2 and r != 2:
                continue
            for p in range(10 ** (k - 1), 10 ** k):
                out.add(int(str(p) * r))
    return sorted(out)


for part in (1, 2):
    total = sum(c for c in candidates(part == 2) if any(a <= c <= b for a, b in ranges))
    print(f"part{part}:", total)
