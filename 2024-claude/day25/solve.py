import sys
blocks = open(sys.argv[1] if len(sys.argv) > 1 else 'input').read().strip().split('\n\n')
locks, keys = [], []
for b in blocks:
    cells = {(r, c) for r, line in enumerate(b.split()) for c, ch in enumerate(line) if ch == '#'}
    (locks if b[0] == '#' else keys).append(cells)
print('part1:', sum(1 for l in locks for k in keys if not (l & k)))
