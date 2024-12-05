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

class Coordinate:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    def __str__(self) -> str:
        return f'({self.row}, {self.col})'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinate):
            return False
        return repr(self) == repr(other)

    def __hash__(self) -> int:
        return hash(repr(self))

class Direction(Enum):
    NORTH = 0
    NORTHEAST = 1
    EAST = 2
    SOUTHEAST = 3
    SOUTH = 4
    SOUTHWEST = 5
    WEST = 6
    NORTHWEST = 7

    @staticmethod
    def values():
        return Direction.__members__.values()

    def next(self, coord: Coordinate) -> Coordinate:
        if self == Direction.NORTH:
            return Coordinate(coord.row - 1, coord.col)
        if self == Direction.NORTHEAST:
            return Coordinate(coord.row - 1, coord.col + 1)
        if self == Direction.EAST:
            return Coordinate(coord.row, coord.col + 1)
        if self == Direction.SOUTHEAST:
            return Coordinate(coord.row + 1, coord.col + 1)
        if self == Direction.SOUTH:
            return Coordinate(coord.row + 1, coord.col)
        if self == Direction.SOUTHWEST:
            return Coordinate(coord.row + 1, coord.col - 1)
        if self == Direction.WEST:
            return Coordinate(coord.row, coord.col - 1)
        if self == Direction.NORTHWEST:
            return Coordinate(coord.row - 1, coord.col - 1)
        raise ValueError(f'Unknown direction {self}')

    def __str__(self) -> str:
        return super().__str__().split('.')[1]

    def __repr__(self) -> str:
        return self.__str__()

class Grid:
    def __init__(self, content: List[List[object]]) -> None:
        self.rows = len(content)
        self.cols = len(content[0])
        self._content = content
        if not all(len(row) == self.cols for row in content):
            raise ValueError(f'grid is not rectangular: {content}')

    def __getitem__(self, row: int) -> List[object]:
        return self._content[row]

    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self._content) + '\n'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Grid):
            return False
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for row in range(self.rows):
            for col in range(self.cols):
                if self[row][col] != other[row][col]:
                    return False
        return True

    def __hash__(self) -> int:
        return hash(repr(self))

    def get(self, coord: Coordinate) -> object:
        if coord.row < 0 or coord.row >= self.rows: return None
        if coord.col < 0 or coord.col >= self.cols: return None
        return self[coord.row][coord.col]

    def contains_at(self, values: List[object], coord: Coordinate, dir: Direction):
        if len(values) == 0:
            return True
        if self.get(coord) == values[0]:
            if args.debug: print(f"{coord} {dir} {values}")
            return self.contains_at(values[1:], dir.next(coord), dir)
        return False

    def find_all(self, value: object) -> List[Coordinate]:
        matches = value if callable(value) else lambda x: x == value
        return [
            Coordinate(row, col)
            for row in range(self.rows)
            for col in range(self.cols)
            if matches(self[row][col])
        ]

    def values_from(self, coord: Coordinate, dir: Direction, count: int):
        values = []
        while count > 0:
            values.append(self.get(coord))
            coord = dir.next(coord)
            count -= 1
        return values

    def find_only(self, value: object) -> Coordinate:
        result = self.find_all(value)
        if len(result) != 1:
            raise ValueError(f'expected exactly one {value}, found {len(result)}')
        return result[0]

    @staticmethod
    def parsefrom(file: TextIO) -> Grid:
        content = []
        for line in file:
            line = line.strip()
            if line == '':
                break
            content.append([c for c in line])
        return Grid(content)

map = Grid.parsefrom(sys.stdin)
if args.debug:
    print(map)

count = 0

if args.part2:
    word = list("MAS")
    reverse = word[::-1]
    for coord in map.find_all(word[1]):
        a = map.values_from(Direction.NORTHWEST.next(coord), Direction.SOUTHEAST, 3)
        if args.debug: print(f"{coord} NW-SE {a}")
        if a != word and a != reverse:
            continue
        b = map.values_from(Direction.SOUTHWEST.next(coord), Direction.NORTHEAST, 3)
        if args.debug: print(f"{coord} SW-NE {b}")
        if b != word and b != reverse:
            continue
        if args.verbose: print(coord)
        count += 1

else: # part1
    letters = list("XMAS")
    for coord in map.find_all(letters[0]):
        for dir in Direction.values():
            if map.contains_at(letters, coord, dir):
                if args.verbose: print(f"{coord} {dir}")
                count += 1

print(count)
