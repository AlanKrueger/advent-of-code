import sys, re
from math import lcm

lines = open(sys.argv[1] if len(sys.argv) > 1 else 'input').read().split('\n')
ins = lines[0].strip()
g = {}
for l in lines[2:]:
    m = re.findall(r'\w+', l)
    if m:
        g[m[0]] = (m[1], m[2])

def steps(s, done):
    n = 0
    while not done(s):
        s = g[s][ins[n % len(ins)] == 'R']
        n += 1
    return n

if 'AAA' in g:
    print('part1:', steps('AAA', lambda s: s == 'ZZZ'))
starts = [k for k in g if k.endswith('A')]
print('part2:', lcm(*(steps(s, lambda s: s.endswith('Z')) for s in starts)))
