# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name

from __future__ import annotations
import argparse
import sys
from typing import List
from strenum import StrEnum

class Pattern(StrEnum):
    ASH = '.'
    ROCK = '#'

def printpattern(pattern: List[List[Pattern]]) -> None:
    for row in pattern:
        print(''.join(row))

def transpose(pattern: List[List[Pattern]]) -> List[List[Pattern]]:
    rows = len(pattern)
    cols = len(pattern[0])
    return [[pattern[row][col] for row in range(rows)] for col in range(cols)]

def diff(a: List[Pattern], b: List[Pattern]) -> int:
    return sum(1 for i in range(len(a)) if a[i] != b[i])

def process(pattern: List[List[Pattern]]) -> int:
    if args.debug:
        printpattern(pattern)
        print()
    rows = len(pattern)

    # scan rows for mirror symmetry
    for row in range(1, rows):
        if args.debug:
            print(f'scanning row {row}')
        matches = True
        smudges = 0
        for i in range(min(row, rows - row)):
            smudges += diff(pattern[row - i - 1], pattern[row + i])
            if smudges > args.smudges:
                matches = False
                break
        if matches and smudges == args.smudges:
            if args.debug:
                print('matching {row}')
            return row
    if args.debug:
        print('no match')
    return 0

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
parser.add_argument('--smudges', type=int, default=0)
parser.set_defaults(debug=False)
args = parser.parse_args()

patterns = []
pattern = []
for line in sys.stdin:
    line = line.strip()
    if line == '':
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append([Pattern(char) for char in line])
patterns.append(pattern)

for i, pattern in enumerate(patterns):
    if args.debug:
        print(f'scanning pattern {i}')
        print()
    print(process(pattern) * 100 + process(transpose(pattern)))
