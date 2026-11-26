import sys

lines = open(sys.argv[1] if len(sys.argv) > 1 else "input").read().split("\n")
matches = []
for line in lines:
    if not line.strip():
        continue
    win, have = line.split(":")[1].split("|")
    matches.append(len(set(win.split()) & set(have.split())))

print("part1:", sum(1 << (m - 1) for m in matches if m))
counts = [1] * len(matches)
for i, m in enumerate(matches):
    for j in range(i + 1, min(i + 1 + m, len(matches))):
        counts[j] += counts[i]
print("part2:", sum(counts))
