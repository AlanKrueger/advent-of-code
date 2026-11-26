import sys
from collections import deque
from math import lcm

def parse(path):
    types, outs = {}, {}
    for line in open(path).read().strip().splitlines():
        a, b = line.split(' -> ')
        if a[0] in '%&':
            types[a[1:]] = a[0]; a = a[1:]
        else:
            types[a] = 'b'
        outs[a] = [x.strip() for x in b.split(',')]
    ins = {}
    for a, ds in outs.items():
        for d in ds:
            ins.setdefault(d, []).append(a)
    return types, outs, ins

def sim(types, outs, ins):
    ff = {m: False for m in types if types[m] == '%'}
    mem = {m: {i: False for i in ins.get(m, [])} for m in types if types[m] == '&'}
    def press(watch=None):
        counts = [0, 0]
        fired = set()
        q = deque([('button', 'broadcaster', False)])
        while q:
            src, dst, hi = q.popleft()
            counts[hi] += 1
            if watch and dst == watch and hi:
                fired.add(src)
            t = types.get(dst)
            if t == 'b':
                send = hi
            elif t == '%':
                if hi: continue
                ff[dst] = not ff[dst]; send = ff[dst]
            elif t == '&':
                mem[dst][src] = hi
                send = not all(mem[dst].values())
            else:
                continue
            for d in outs[dst]:
                q.append((dst, d, send))
        return counts, fired
    return press

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'input'
    types, outs, ins = parse(path)
    press = sim(types, outs, ins)
    lo = hi = 0
    for _ in range(1000):
        (l, h), _f = press()
        lo += l; hi += h
    print(f'part1: {lo*hi}')
    if 'rx' not in ins:
        return
    (feeder,) = ins['rx']
    srcs = set(ins[feeder])
    press = sim(types, outs, ins)
    first = {}
    n = 0
    while len(first) < len(srcs):
        n += 1
        _c, fired = press(feeder)
        for s in fired:
            first.setdefault(s, n)
    print(f'part2: {lcm(*first.values())}')

main()
