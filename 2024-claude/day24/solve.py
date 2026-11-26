import sys

def main():
    fn = sys.argv[1] if len(sys.argv) > 1 else 'input'
    top, bot = open(fn).read().strip().split('\n\n')
    vals = {}
    for l in top.splitlines():
        k, v = l.split(': ')
        vals[k] = int(v)
    gates = []
    for l in bot.splitlines():
        a, op, b, _, o = l.split()
        gates.append((a, op, b, o))
    by_out = {g[3]: g for g in gates}
    memo = dict(vals)
    def ev(w):
        if w not in memo:
            a, op, b, _ = by_out[w]
            x, y = ev(a), ev(b)
            memo[w] = x & y if op == 'AND' else x | y if op == 'OR' else x ^ y
        return memo[w]
    zs = sorted((w for w in by_out if w.startswith('z')), reverse=True)
    print('part1:', int(''.join(str(ev(z)) for z in zs), 2))
    if len(sys.argv) > 2:
        return
    # Part 2: structural rules for a ripple-carry adder.
    last = zs[0]
    uses = {}
    for a, op, b, o in gates:
        uses.setdefault(a, []).append(op)
        uses.setdefault(b, []).append(op)
    bad = set()
    for a, op, b, o in gates:
        xy = a[0] in 'xy' and b[0] in 'xy'
        first = {a, b} == {'x00', 'y00'}
        if o.startswith('z') and o != last and op != 'XOR':
            bad.add(o)
        if op == 'XOR' and not xy and not o.startswith('z'):
            bad.add(o)
        if op == 'XOR' and xy and not first and 'XOR' not in uses.get(o, []):
            bad.add(o)
        if op == 'AND' and not first and 'OR' not in uses.get(o, []):
            bad.add(o)
        if o == last and op != 'OR':
            bad.add(o)
    print('part2:', ','.join(sorted(bad)))

main()
