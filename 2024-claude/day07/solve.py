import sys

def ok(target, nums, concat):
    # work backwards from the target
    def rec(t, i):
        n = nums[i]
        if i == 0:
            return t == n
        if t > n and rec(t - n, i - 1):
            return True
        if t % n == 0 and rec(t // n, i - 1):
            return True
        if concat:
            s, ns = str(t), str(n)
            if len(s) > len(ns) and s.endswith(ns) and rec(int(s[:-len(ns)]), i - 1):
                return True
        return False
    return rec(target, len(nums) - 1)

eqs = []
for line in open(sys.argv[1] if len(sys.argv) > 1 else 'input'):
    if line.strip():
        a, b = line.split(':')
        eqs.append((int(a), list(map(int, b.split()))))
print('part1:', sum(t for t, n in eqs if ok(t, n, False)))
print('part2:', sum(t for t, n in eqs if ok(t, n, True)))
