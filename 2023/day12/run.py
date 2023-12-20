# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name

from __future__ import annotations
import argparse
import sys
from functools import cache as memoized
from typing import List
from strenum import StrEnum


class Condition(StrEnum):
    OPERATIONAL = '.'
    DAMAGED = '#'
    UNKNOWN = '?'

    @memoized
    def known(self) -> List[Condition]:
        if self == Condition.UNKNOWN:
            return [Condition.DAMAGED, Condition.OPERATIONAL]
        return [self]

def count(
        conditions: List[Condition],
        i: int,
        groups: List[int],
        j: int) -> int:
    dump(conditions, i, groups, j, "enter")
    if i >= len(conditions):
        if not all(group == 0 for group in groups):
            dump(conditions, i, groups, j, f'bailing - {groups} not all zeros')
            return 0
        dump(conditions, i, groups, j, "match <--")
        return 1
    if any(group < 0 for group in groups):
        dump(conditions, i, groups, j, f'bailing - {groups} has negative')
        return 0
    if j > len(groups):
        dump(conditions, i, groups, j, "bailing - j >= len(groups)")
        return 0
    total = 0
    saveCondition = conditions[i]
    saveGroup = groups[j] if j < len(groups) else 0
    for condition in conditions[i].known():
        conditions[i] = condition
        prevDamaged = conditions[i - 1] == Condition.DAMAGED if i > 0 else False
        hereOperational = conditions[i] == Condition.OPERATIONAL
        transition = prevDamaged and hereOperational
        nextj = j + 1 if transition else j
        if j < len(groups):
            groups[j] = saveGroup - 1 if conditions[i] == Condition.DAMAGED else saveGroup
        elif conditions[i] == Condition.DAMAGED:
            dump(conditions, i, groups, j, f'skipping - {groups} has no more groups')
            continue
        dump(conditions, i, groups, j, f'recurse {"transition" if transition else ""}')
        total += count(conditions, i + 1, groups, nextj)
        conditions[i] = saveCondition
        if j < len(groups):
            groups[j] = saveGroup
        dump(conditions, i, groups, j, "return")
    return total

def dump(
        conditions: List[Condition],
        i: int,
        groups: List[int],
        j: int,
        message: str):
    if args.debug:
        s = "".join(conditions)
        ps = len(s) - i - 1
        g = str(groups)
        bg = sum([len(str(g)) for g in groups[:j]]) + 2 * j
        print(f'{s} {g} {message}')
        print(f'{" " * i}^{" " * ps}  {" " * bg}^')

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
parser.add_argument('--part2', action='store_true')
parser.add_argument('--no-part2', action='store_false', dest='part2')
parser.set_defaults(debug=False, part2=False)
args = parser.parse_args()

for line in sys.stdin:
    pieces = line.strip().split()
    conditions = [Condition(value) for value in pieces[0]]
    counts = [int(num) for num in pieces[1].split(',')]
    if args.part2:
        base = list(conditions)
        for _ in range(4):
            conditions.append(Condition.UNKNOWN)
            conditions.extend(base)
        counts = counts * 5
    print(count(conditions, 0, counts, 0))
