# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name, too-few-public-methods, redefined-builtin

from __future__ import annotations
import argparse
import sys
from typing import List
from typing import TextIO
from enum import Enum
from strenum import StrEnum

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

class Fixture(StrEnum):
    NS_SPLITTER = '|'
    EW_SPLITTER = '-'
    NE_SW_MIRROR = '/'
    NW_SE_MIRROR = '\\'
    EMPTY = '.'

    def alter(self, beam: Beam) -> List[Beam]:
        if self == Fixture.NS_SPLITTER:
            if beam.dir in (Direction.WEST, Direction.EAST):
                return [beam.turn(Direction.NORTH), beam.turn(Direction.SOUTH)]
            # fall through
        elif self == Fixture.EW_SPLITTER:
            if beam.dir in (Direction.NORTH, Direction.SOUTH):
                return [beam.turn(Direction.WEST), beam.turn(Direction.EAST)]
            # fall through
        elif self == Fixture.NE_SW_MIRROR:
            if beam.dir == Direction.NORTH:
                return [beam.turn(Direction.EAST)]
            if beam.dir == Direction.EAST:
                return [beam.turn(Direction.NORTH)]
            if beam.dir == Direction.SOUTH:
                return [beam.turn(Direction.WEST)]
            if beam.dir == Direction.WEST:
                return [beam.turn(Direction.SOUTH)]
        elif self == Fixture.NW_SE_MIRROR:
            if beam.dir == Direction.NORTH:
                return [beam.turn(Direction.WEST)]
            if beam.dir == Direction.EAST:
                return [beam.turn(Direction.SOUTH)]
            if beam.dir == Direction.SOUTH:
                return [beam.turn(Direction.EAST)]
            if beam.dir == Direction.WEST:
                return [beam.turn(Direction.NORTH)]
        # otherwise just propagate
        return [beam.next()]

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

class Beam:
    def __init__(self, coord: Coordinate, dir: Direction) -> None:
        self.coord = coord
        self.dir = dir

    def next(self) -> Beam:
        return Beam(self.dir.next(self.coord), self.dir)

    def turn(self, dir: Direction) -> Beam:
        return Beam(dir.next(self.coord), dir)

    def __str__(self) -> str:
        return f'{self.coord} {self.dir}'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Beam):
            return False
        return repr(self) == repr(other)

    def __hash__(self) -> int:
        return hash(repr(self))

class Grid:
    def __init__(self, content: List[List[object]]) -> None:
        self.rows = len(content)
        self.cols = len(content[0])
        if not all(len(row) == self.cols for row in content):
            raise ValueError('Grid must be rectangular')
        self.content = content
        self._energized = [[False for _ in range(self.cols)] for _ in range(self.rows)]

    def inbounds(self, coord: Coordinate) -> bool:
        return 0 <= coord.row < self.rows and 0 <= coord.col < self.cols

    def propagate(self, beam: Beam) -> List[Beam]:
        if not self.inbounds(beam.coord):
            return []
        self._energized[beam.coord.row][beam.coord.col] = True
        fixture = self.content[beam.coord.row][beam.coord.col]
        next = fixture.alter(beam)
        if args.debug:
            print(f'{beam} + {fixture} -> {next}')
        return next

    def energize(self, beams: List[Beam]) -> int:
        self._energized = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        energized = 0
        beams = set(beams)
        seen = set(beams)
        while len(beams) > 0:
            if args.debug:
                print('next cycle')
                print()

            nextbeams = set()
            for beam in beams:
                nextbeams.update(self.propagate(beam))
            energized = sum(sum(col for col in row) for row in self._energized)
            beams = nextbeams.difference(seen)
            seen.update(beams)

            if args.debug:
                print('energized:')
                for row in self._energized:
                    print(''.join('#' if col else '.' for col in row))
                print()

        return energized

    @staticmethod
    def parsefrom(file: TextIO) -> Grid:
        content = []
        for line in file:
            content.append([Fixture(ch) for ch in line.strip()])
        return Grid(content)

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
parser.add_argument('--part2', action='store_true')
parser.set_defaults(debug=False, part2=False)
args = parser.parse_args()

grid = Grid.parsefrom(sys.stdin)

if args.debug:
    for row in grid.content:
        print(''.join(str(fixture) for fixture in row))
    print()

if not args.part2:
    print(grid.energize([Beam(Coordinate(0, 0), Direction.EAST)]))
else:
    mx = 0
    # north edge
    if args.debug:
        print(f'{grid.rows} x {grid.cols}')
        print('north edge')
    for col in range(grid.cols):
        coord = Coordinate(0, col)
        if args.debug:
            print(coord)
        mx = max(mx, grid.energize([Beam(coord, Direction.SOUTH)]))
    # west edge
    if args.debug:
        print('west edge')
    for row in range(grid.rows):
        coord = Coordinate(row, 0)
        if args.debug:
            print(coord)
        mx = max(mx, grid.energize([Beam(coord, Direction.EAST)]))
    # south edge
    if args.debug:
        print('south edge')
    for col in range(grid.cols):
        coord = Coordinate(grid.rows - 1, col)
        if args.debug:
            print(coord)
        mx = max(mx, grid.energize([Beam(coord, Direction.NORTH)]))
    # east edge
    if args.debug:
        print('east edge')
    for row in range(grid.rows):
        coord = Coordinate(row, grid.cols - 1)
        if args.debug:
            print(coord)
        mx = max(mx, grid.energize([Beam(coord, Direction.WEST)]))
    print(mx)