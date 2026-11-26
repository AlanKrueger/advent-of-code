import sys, re
from math import prod

def main():
    fn = sys.argv[1] if len(sys.argv) > 1 else "input"
    wf_txt, parts_txt = open(fn).read().strip().split("\n\n")
    wfs = {}
    for line in wf_txt.splitlines():
        name, body = line[:-1].split("{")
        rules = []
        for r in body.split(","):
            if ":" in r:
                cond, dst = r.split(":")
                rules.append((cond[0], cond[1], int(cond[2:]), dst))
            else:
                rules.append((None, None, None, r))
        wfs[name] = rules
    total = 0
    for line in parts_txt.splitlines():
        p = {k: int(v) for k, v in re.findall(r"(\w)=(\d+)", line)}
        w = "in"
        while w not in "AR":
            for k, op, v, dst in wfs[w]:
                if k is None or (op == "<" and p[k] < v) or (op == ">" and p[k] > v):
                    w = dst
                    break
        if w == "A":
            total += sum(p.values())
    print(f"part1: {total}")

    def count(w, rng):
        if w == "R":
            return 0
        if w == "A":
            return prod(hi - lo + 1 for lo, hi in rng.values())
        n = 0
        for k, op, v, dst in wfs[w]:
            if k is None:
                return n + count(dst, rng)
            lo, hi = rng[k]
            if op == "<":
                t, f = (lo, min(hi, v - 1)), (max(lo, v), hi)
            else:
                t, f = (max(lo, v + 1), hi), (lo, min(hi, v))
            if t[0] <= t[1]:
                n += count(dst, {**rng, k: t})
            if f[0] > f[1]:
                return n
            rng = {**rng, k: f}
        return n
    print(f"part2: {count('in', {c: (1, 4000) for c in 'xmas'})}")

main()
