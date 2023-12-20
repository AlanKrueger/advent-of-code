# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name, non-ascii-name, too-few-public-methods

from __future__ import annotations
import sys

def HASH(string):
    value = 0
    for ch in string:
        value += ord(ch)
        value *= 17
        value %= 256
    return value

for line in sys.stdin:
    for part in line.strip().split(','):
        print(HASH(part))
