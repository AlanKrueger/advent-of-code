# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name, non-ascii-name, too-few-public-methods, method-cache-max-size-none, redefined-builtin

from __future__ import annotations
import argparse
import sys
from typing import Callable, Optional, List, TextIO
from enum import Enum
from strenum import StrEnum

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--part2', action='store_true')
parser.add_argument('--steps', type=int, default=1)
parser.set_defaults(debug=False, verbose=False, part2=False)
args = parser.parse_args()

left=[]
right=[]

for line in sys.stdin:
    (a, b) = line.split(maxsplit=2)
    left.append(int(a))
    right.append(int(b))

left.sort()
right.sort()

def part1(left: List[int], right: List[int]):
    total_dist = 0
    for i in range(len(left)):
        total_dist += abs(left[i] - right[i])
    return total_dist

def part2(left: List[int], right: List[int]):
    total_score = 0
    for i in range(len(left)):
        total_score += left[i] * right.count(left[i])
    return total_score

behavior = part2 if args.part2 else part1
print(behavior(left, right))
