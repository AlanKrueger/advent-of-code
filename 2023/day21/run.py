# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name, non-ascii-name, too-few-public-methods, method-cache-max-size-none, redefined-builtin

from __future__ import annotations
import argparse
import sys
from typing import Callable, List, TextIO
from enum import Enum
from strenum import StrEnum

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
parser.add_argument('--part2', action='store_true')
parser.add_argument('--steps', type=int, default=1)
parser.set_defaults(debug=False, part2=False)
args = parser.parse_args()

class Content(StrEnum):
    EMPTY = '.'
    WALL = '#'
    START = 'S'
    PLOT = 'O'

    def __repr__(self) -> str:
        return super().__str__()

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
    EAST = 1
    SOUTH = 2
    WEST = 3

    def next(self, coord: Coordinate) -> Coordinate:
        if self == Direction.NORTH:
            return Coordinate(coord.row - 1, coord.col)
        if self == Direction.EAST:
            return Coordinate(coord.row, coord.col + 1)
        if self == Direction.SOUTH:
            return Coordinate(coord.row + 1, coord.col)
        if self == Direction.WEST:
            return Coordinate(coord.row, coord.col - 1)
        raise ValueError(f'Unknown direction {self}')

    def __str__(self) -> str:
        return super().__str__().split('.')[1][0]

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

    def find_all(self, value: object) -> List[Coordinate]:
        matches = value if callable(value) else lambda x: x == value
        return [
            Coordinate(row, col)
            for row in range(self.rows)
            for col in range(self.cols)
            if matches(self[row][col])
        ]

    def find_only(self, value: object) -> Coordinate:
        result = self.find_all(value)
        if len(result) != 1:
            raise ValueError(f'expected exactly one {value}, found {len(result)}')
        return result[0]

    @staticmethod
    def parsefrom(file: TextIO, convert: Callable) -> Grid:
        content = []
        for line in file:
            line = line.strip()
            if line == '':
                break
            content.append([convert(c) for c in line])
        return Grid(content)

    def advance(self) -> Grid:
        content = [list(row) for row in self._content]
        for row in range(self.rows):
            for col in range(self.cols):
                if self[row][col] == Content.START or self[row][col] == Content.PLOT:
                    coord = Coordinate(row, col)
                    content[row][col] = Content.EMPTY
                    for direction in Direction:
                        next = direction.next(coord)
                        if self[next.row][next.col] != Content.WALL:
                            content[next.row][next.col] = Content.PLOT
        return Grid(content)

map = Grid.parsefrom(sys.stdin, Content)
if args.debug:
    print(map)

for _ in range(args.steps):
    map = map.advance()
    if args.debug:
        print(map)

if not args.part2:
    print(len(map.find_all(Content.PLOT)))
