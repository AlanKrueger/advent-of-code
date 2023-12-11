import sys

from typing import List

def _gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    if a < b:
        (a, b) = (b, a)
    r = a % b
    q = a // b
    return _gcd(b, r)

def gcd(a: List[int]) -> int:
    if len(a) < 2:
        raise ValueError("need at least two values")
    d = a[0]
    for v in a[1:]:
        d = _gcd(d, v)
    return d

def _lcm(a: int, b: int) -> int:
    return a * (b // _gcd(a, b))

def lcm(a: List[int]) -> int:
    if len(a) < 2:
        raise ValueError("need at least two values")
    m = a[0]
    for v in a[1:]:
        m = _lcm(m, v)
    return m

values = [int(line) for line in sys.stdin]
print(lcm(values))