import sys
from collections import Counter

def kind(h):
    return sorted(Counter(h).values(), reverse=True)

def kind_joker(h):
    j = h.count('J')
    c = sorted(Counter(x for x in h if x != 'J').values(), reverse=True) or [0]
    c[0] += j
    return c

def total(hands, order, kf):
    key = lambda hb: (kf(hb[0]), [order.index(c) for c in hb[0]])
    return sum(i * int(b) for i, (h, b) in enumerate(sorted(hands, key=key), 1))

hands = [l.split() for l in open(sys.argv[1] if len(sys.argv) > 1 else 'input').read().split('\n') if l.strip()]
print('part1:', total(hands, '23456789TJQKA', kind))
print('part2:', total(hands, 'J23456789TQKA', kind_joker))
