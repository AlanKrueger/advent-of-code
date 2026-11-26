import sys

def main():
    fn = sys.argv[1] if len(sys.argv) > 1 else 'input'
    blocks = open(fn).read().strip().split('\n\n')
    seeds = list(map(int, blocks[0].split(':')[1].split()))
    maps = [[tuple(map(int, l.split())) for l in b.splitlines()[1:]] for b in blocks[1:]]

    def run(ranges):  # list of [lo, hi)
        for m in maps:
            out = []
            todo = list(ranges)
            while todo:
                lo, hi = todo.pop()
                for d, s, n in m:
                    a, b = max(lo, s), min(hi, s + n)
                    if a < b:
                        out.append((a - s + d, b - s + d))
                        if lo < a: todo.append((lo, a))
                        if b < hi: todo.append((b, hi))
                        break
                else:
                    out.append((lo, hi))
            ranges = out
        return min(lo for lo, _ in ranges)

    print('part1:', run([(x, x + 1) for x in seeds]))
    print('part2:', run([(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]))

main()
