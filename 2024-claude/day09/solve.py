import sys

s = open(sys.argv[1] if len(sys.argv) > 1 else 'input').read().strip()

# part 1
blocks = []
for i, c in enumerate(s):
    blocks += [i // 2 if i % 2 == 0 else -1] * int(c)
l, r = 0, len(blocks) - 1
while True:
    while l < r and blocks[l] != -1: l += 1
    while l < r and blocks[r] == -1: r -= 1
    if l >= r: break
    blocks[l], blocks[r] = blocks[r], -1
print('part1:', sum(i * b for i, b in enumerate(blocks) if b != -1))

# part 2: move whole files, highest ID first, to leftmost fitting gap left of them
files, gaps, pos = [], [], 0
for i, c in enumerate(s):
    n = int(c)
    if i % 2 == 0: files.append([pos, n])
    elif n: gaps.append([pos, n])
    pos += n
for fid in range(len(files) - 1, -1, -1):
    fp, fl = files[fid]
    for g in gaps:
        if g[0] >= fp: break
        if g[1] >= fl:
            files[fid][0] = g[0]
            g[0] += fl; g[1] -= fl
            break
print('part2:', sum(fid * (p + k) for fid, (p, n) in enumerate(files) for k in range(n)))
