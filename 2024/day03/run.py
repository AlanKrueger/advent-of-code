# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name, non-ascii-name, too-few-public-methods, method-cache-max-size-none, redefined-builtin

from __future__ import annotations
import argparse
import re
import sys
from typing import Callable, Optional, List, TextIO
from enum import Enum
from strenum import StrEnum

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--part2', action='store_true')
parser.set_defaults(debug=False, verbose=False, part2=False)
args = parser.parse_args()

def _debug(message: str):
    if args.debug:
        print(message)

def _verbose(message: str):
    if args.verbose:
        print(message)

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")

total = 0
enabled = True
for line in sys.stdin:
    for match in pattern.finditer(line):
        operation = match.group(0)
        if operation.startswith("mul"):
            if enabled:
                a = int(match.group(1))
                b = int(match.group(2))
                if args.verbose: print(f"{a}*{b}")
                total += a * b
        elif args.part2:
                enabled = not operation.startswith("don't")

print(total)
