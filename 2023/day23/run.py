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
        return self.row == other.row and self.col == other.col

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

    @staticmethod
    def values(starting_with: Optional[Direction] = None) -> List[Direction]:
        if starting_with is None:
            return list(Direction)
        return list(Direction)[starting_with.value:]

    def reverse(self) -> Direction:
        if self == Direction.NORTH:
            return Direction.SOUTH
        if self == Direction.EAST:
            return Direction.WEST
        if self == Direction.SOUTH:
            return Direction.NORTH
        if self == Direction.WEST:
            return Direction.EAST
        return None

    def succ(self) -> Direction:
        if self == Direction.NORTH:
            return Direction.EAST
        if self == Direction.EAST:
            return Direction.SOUTH
        if self == Direction.SOUTH:
            return Direction.WEST
        return None


class Content(StrEnum):
    EMPTY = '.'
    WALL = '#'
    START = 'S'
    PATH = 'O'
    SLOPE_NORTH = '^'
    SLOPE_WEST = '<'
    SLOPE_SOUTH = 'v'
    SLOPE_EAST = '>'

    def __repr__(self) -> str:
        return super().__str__()

    def can_enter(self, dir: Direction):
        if self == Content.EMPTY:
            return True
        if args.part2 and self in [
                Content.SLOPE_NORTH, Content.SLOPE_WEST, Content.SLOPE_SOUTH, Content.SLOPE_EAST]:
            return True
        if self == Content.SLOPE_NORTH and dir == Direction.NORTH:
            return True
        if self == Content.SLOPE_WEST and dir == Direction.WEST:
            return True
        if self == Content.SLOPE_SOUTH and dir == Direction.SOUTH:
            return True
        if self == Content.SLOPE_EAST and dir == Direction.EAST:
            return True
        return False


class Grid:
    def __init__(self, content: List[List[object]]) -> None:
        self.rows = len(content)
        self.cols = len(content[0])
        self._content = content
        if not all(len(row) == self.cols for row in content):
            raise ValueError(f'grid is not rectangular: {content}')
        self.start = self._empty_in_row(0)
        self.end = self._empty_in_row(self.rows - 1)

    def _empty_in_row(self, row: int) -> Coordinate:
        pos = next(
            (col for col in range(self.cols)
             if self[row][col] == Content.EMPTY),
            None)
        return None if pos is None else Coordinate(row, pos)

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

    @staticmethod
    def parsefrom(file: TextIO, convert: Callable) -> Grid:
        content = []
        for line in file:
            line = line.strip()
            if line == '':
                break
            content.append([convert(c) for c in line])
        return Grid(content)

    def inbounds(self, coord: Coordinate) -> bool:
        return 0 <= coord.row < self.rows and 0 <= coord.col < self.cols


class PathFinder:
    def __init__(self, grid: Grid) -> None:
        self.grid = grid
        self.pos = grid.start
        self.dirs = []

    def find_longest_path(self) -> int:
        self.pos = self.grid.start
        self.grid[self.pos.row][self.pos.col] = Content.START
        max_length = 0
        while self.advance():
            if self.pos == self.grid.end:
                if args.verbose:
                    print(f'found path of length {self.length()}')
                    print(self.grid)
                max_length = max(max_length, self.length())
        return max_length

    def advance(self, dir_hint: Optional[Direction] = None) -> bool:
        while True:
            for dir in Direction.values(dir_hint):
                next = dir.next(self.pos)
                if self.grid.inbounds(next) and self.grid[next.row][next.col].can_enter(dir):
                    if self.grid[next.row][next.col] == Content.EMPTY:
                        self.grid[next.row][next.col] = Content.PATH
                    self.pos = next
                    self.dirs.append(dir)
                    if args.debug:
                        print(f'advance {dir} to {self.pos}')
                        print(self.grid)
                    return True
            while True:
                last = self.retreat()
                if last is None:
                    return False
                dir_hint = last.succ()
                if dir_hint is not None:
                    break

    def retreat(self) -> Direction:
        if len(self.dirs) == 0:
            return None
        last = self.dirs.pop()
        if last is not None:
            if self.grid[self.pos.row][self.pos.col] == Content.PATH:
                self.grid[self.pos.row][self.pos.col] = Content.EMPTY
            self.pos = last.reverse().next(self.pos)
            if args.debug:
                print(f'retreat {last.reverse()} to {self.pos}')
        return last

    def length(self):
        return len(self.dirs)


map = Grid.parsefrom(sys.stdin, Content)
if args.debug:
    print(map)

pathfinder = PathFinder(map)
print(pathfinder.find_longest_path())
