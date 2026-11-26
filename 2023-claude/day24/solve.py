import sys, re
from fractions import Fraction as F

fn = sys.argv[1] if len(sys.argv) > 1 else "input"
lo = int(sys.argv[2]) if len(sys.argv) > 2 else 200000000000000
hi = int(sys.argv[3]) if len(sys.argv) > 3 else 400000000000000
H = [list(map(int, re.findall(r"-?\d+", l))) for l in open(fn) if l.strip()]

cnt = 0
for i in range(len(H)):
    x1, y1, _, a1, b1, _ = H[i]
    for j in range(i + 1, len(H)):
        x2, y2, _, a2, b2, _ = H[j]
        d = a1 * (-b2) - (-a2) * b1
        if d == 0:
            continue
        # x1 + a1 t = x2 + a2 s ; y1 + b1 t = y2 + b2 s
        t = F((x2 - x1) * (-b2) - (-a2) * (y2 - y1), d)
        s = F(a1 * (y2 - y1) - b1 * (x2 - x1), d)
        if t < 0 or s < 0:
            continue
        x, y = x1 + a1 * t, y1 + b1 * t
        if lo <= x <= hi and lo <= y <= hi:
            cnt += 1
print("part1:", cnt)

def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def sub(a, b):
    return [x - y for x, y in zip(a, b)]

# P x (vi - vj) + (pi - pj) x V = pi x vi - pj x vj
rows = []
for i, j in [(0, 1), (0, 2), (1, 2)]:
    pi, vi, pj, vj = H[i][:3], H[i][3:], H[j][:3], H[j][3:]
    dv, dp = sub(vi, vj), sub(pi, pj)
    rhs = sub(cross(pi, vi), cross(pj, vj))
    cols = []
    for k in range(6):
        e = [0] * 6; e[k] = 1
        cols.append([x + y for x, y in zip(cross(e[:3], dv), cross(dp, e[3:]))])
    for r in range(3):
        rows.append([F(cols[k][r]) for k in range(6)] + [F(rhs[r])])
n = 6
# use all 9 rows; least-squares not needed, eliminate with pivoting
M = rows
r = 0
piv = []
for c in range(n):
    p = next((k for k in range(r, len(M)) if M[k][c] != 0), None)
    if p is None:
        continue
    M[r], M[p] = M[p], M[r]
    M[r] = [x / M[r][c] for x in M[r]]
    for k in range(len(M)):
        if k != r and M[k][c] != 0:
            f = M[k][c]
            M[k] = [x - f * y for x, y in zip(M[k], M[r])]
    piv.append(c); r += 1
sol = [M[k][n] for k in range(n)]
print("part2:", int(sum(sol[:3])))
