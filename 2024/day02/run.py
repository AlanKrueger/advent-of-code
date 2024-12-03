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

def _sign(value: int) -> int:
    if value < 0:
        return -1
    if value > 0:
        return 1
    return 0

def _debug(message: str):
    if args.debug:
        print(message)

def _verbose(message: str):
    if args.verbose:
        print(message)

class Report:
    def __init__(self, levels: List[int]):
        self.levels = levels

    def __str__(self):
        return self.levels.__str__()

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def parse(line: str) -> Report:
        levels = list(map(int, line.split()))
        return Report(levels)

    @staticmethod
    def parse_many(file: TextIO) -> List[Report]:
        reports = []
        for line in file:
            reports.append(Report.parse(line))
        return reports

    @staticmethod
    def safe_skip(levels: List[int]):
        diff = levels[1] - levels[0]
        _debug(f"> {levels} [1] diff = {diff}")
        if abs(diff) < 1 or abs(diff) > 3:
            _verbose(f"> {levels} not safe: [1] diff {diff}")
            return False

        initial_sign = _sign(diff)
        _debug(f"> {levels} [1] sign = {initial_sign}")

        for i in range(2, len(levels)):
            diff = levels[i] - levels[i - 1]
            _debug(f"> {levels} [{i}] diff = {diff}")
            if abs(diff) < 1 or abs(diff) > 3:
                _verbose(f"> {levels} not safe: [{i}] diff {diff}")
                return False
            sign = _sign(diff)
            _debug(f"> {levels} [{i}] sign = {sign}")
            if sign != initial_sign:
                _verbose(f"> {levels} not safe: [{i}] sign {sign} != {initial_sign}")
                return False

        if args.verbose:
            print(f"{levels} safe")
        return True

    def safe(self) -> bool:
        if args.part2:
            for skip in range(-1, len(self.levels)):
                _verbose(f"{self.levels} trying {"no" if skip < 0 else skip} skip")
                levels = self.levels
                if skip >= 0:
                    levels = levels.copy()
                    levels.pop(skip)
                if self.safe_skip(levels):
                    _verbose(f"{self.levels} safe with {"no" if skip < 0 else skip} skip")
                    return True
            _verbose(f"{self.levels} unsafe with any skip")
            return False
        # part 1
        return self.safe_skip(self.levels)

reports = Report.parse_many(sys.stdin)

num_safe = len(list(filter(lambda report: report.safe(), reports)))
print(num_safe)
