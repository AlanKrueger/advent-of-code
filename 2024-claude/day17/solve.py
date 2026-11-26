import re, sys

def run(prog, a, b, c):
    ip, out = 0, []
    while ip < len(prog):
        op, x = prog[ip], prog[ip + 1]
        combo = [0, 1, 2, 3, a, b, c, None][x]
        if op == 0: a >>= combo
        elif op == 1: b ^= x
        elif op == 2: b = combo & 7
        elif op == 3 and a: ip = x; continue
        elif op == 4: b ^= c
        elif op == 5: out.append(combo & 7)
        elif op == 6: b = a >> combo
        elif op == 7: c = a >> combo
        ip += 2
    return out

def part2(prog, b, c):
    # Program consumes A 3 bits per loop; build A from the last output backwards.
    cands = [0]
    for i in range(len(prog) - 1, -1, -1):
        cands = [a * 8 + d for a in cands for d in range(8)
                 if run(prog, a * 8 + d, b, c) == prog[i:]]
    cands = [x for x in cands if x > 0]
    return min(cands) if cands else None

nums = list(map(int, re.findall(r"\d+", open(sys.argv[1] if len(sys.argv) > 1 else "input").read())))
a, b, c, prog = nums[0], nums[1], nums[2], nums[3:]
print("part1:", ",".join(map(str, run(prog, a, b, c))))
print("part2:", part2(prog, b, c))
