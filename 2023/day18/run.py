# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name, too-few-public-methods, redefined-builtin

from __future__ import annotations
import argparse
import sys
from typing import Optional
from scipy.sparse import lil_matrix
from strenum import StrEnum

OPEN = 0
TRENCH = 1

class Direction(StrEnum):
    NORTH = 'U'
    EAST = 'R'
    SOUTH = 'D'
    WEST = 'L'

    def next(self, coord: Coordinate, dist: Optional[int] = 1) -> Coordinate:
        if self == Direction.NORTH:
            return Coordinate(coord.row - dist, coord.col)
        if self == Direction.EAST:
            return Coordinate(coord.row, coord.col + dist)
        if self == Direction.SOUTH:
            return Coordinate(coord.row + dist, coord.col)
        if self == Direction.WEST:
            return Coordinate(coord.row, coord.col - dist)
        raise ValueError(f'Unknown direction {self}')

    def reverse(self) -> Direction:
        if self == Direction.NORTH:
            return Direction.SOUTH
        if self == Direction.EAST:
            return Direction.WEST
        if self == Direction.SOUTH:
            return Direction.NORTH
        if self == Direction.WEST:
            return Direction.EAST
        raise ValueError(f'Unknown direction {self}')

    def glyph(self) -> str:
        if self == Direction.NORTH:
            return '^'
        if self == Direction.EAST:
            return '>'
        if self == Direction.SOUTH:
            return 'v'
        if self == Direction.WEST:
            return '<'
        raise ValueError(f'Unknown direction {self}')

    def __repr__(self) -> str:
        return self.__str__()

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

class SparseGrid:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.content = lil_matrix((rows, cols), dtype=int)

    def inbounds(self, coord: Coordinate) -> bool:
        return 0 <= coord.row < self.rows and 0 <= coord.col < self.cols

    def trench(self, a: Coordinate, b: Coordinate) -> None:
        if a.row == b.row:
            cols = sorted([a.col, b.col])
            self.content[a.row, cols[0]:cols[1] + 1] = TRENCH
        else:
            rows = sorted([a.row, b.row])
            self.content[rows[0]:rows[1] + 1, a.col] = TRENCH

    def digInterior(self) -> None:
        overlay = lil_matrix((self.rows, self.cols), dtype=int)
        for row in range(self.rows):
            top = False
            bottom = False
            for col in range(self.cols):
                if self.content[row, col] == TRENCH:
                    if row > 0 and self.content[row - 1, col] == TRENCH:
                        top = not top
                    if row + 1 < rows and self.content[row + 1, col] == TRENCH:
                        bottom = not bottom
                else:
                    if top and bottom:
                        overlay[row, col] = TRENCH
        self.content += overlay

    def volume(self) -> int:
        return self.content.count_nonzero()

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--debug', action='store_true')
parser.add_argument('--part2', action='store_true')
parser.set_defaults(verbose=False, debug=False, part2=False)
args = parser.parse_args()

if args.debug:
    args.verbose = True

plan = [tuple(line.strip().split()) for line in sys.stdin]
plan = [(Direction(dir), int(dist), color[1:8]) for (dir, dist, color) in plan]

if args.part2:
    dirs = [Direction(ch) for ch in "RDLU"]
    plan = [
        (dirs[int(color[6])], int(color[1:6], 16), color)
        for (_, _, color) in plan
    ]

if args.debug and not args.part2:
    for step in plan:
        print(step)
    print()

if args.verbose:
    print('Computing bounding box...')
pos = Coordinate(0, 0)
coords = [pos]
if args.debug:
    print(f'Initial position: {pos}')
for step in plan:
    (dir, dist, color) = step
    pos = dir.next(pos, dist)
    coords.append(pos)
    if args.debug:
        print(f'After {step}: {pos}')
if args.debug:
    print()

mn = Coordinate(0, 0)
mx = Coordinate(0, 0)
for coord in coords:
    mn = Coordinate(min(mn.row, coord.row), min(mn.col, coord.col))
    mx = Coordinate(max(mx.row, coord.row), max(mx.col, coord.col))

if args.verbose:
    print('Building grid...')
rows = mx.row - mn.row + 1
cols = mx.col - mn.col + 1
grid = SparseGrid(rows, cols)

if args.verbose:
    print('Trenching...')
pos = Coordinate(-mn.row, -mn.col)
for step in plan:
    (dir, dist, color) = step
    next = dir.next(pos, dist)
    grid.trench(pos, next)
    pos = next
    if args.debug:
        print(f'After {step}: {pos}')
        if not args.part2:
            for row in grid.content.A:
                print(''.join('#' if v > 0 else '.' for v in row))
        print()

if args.verbose:
    print('Digging interior...')
grid.digInterior()

if args.debug:
    for row in grid.content.A:
        print(''.join('#' if v > 0 else '.' for v in row))
    print()

print(grid.volume())
