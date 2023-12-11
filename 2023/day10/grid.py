# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name

from __future__ import annotations

from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import TextIO

import math
import sys

from functools import cache as memoized
from strenum import StrEnum

class Direction(StrEnum):
    NORTH = 'N'
    WEST = 'W'
    EAST = 'E'
    SOUTH = 'S'

    @memoized
    def opposite(self):
        match self:
            case Direction.NORTH:
                return Direction.SOUTH
            case Direction.WEST:
                return Direction.EAST
            case Direction.EAST:
                return Direction.WEST
            case Direction.SOUTH:
                return Direction.NORTH
        raise ValueError(f'unexpected direction: {self}')

class PipeType(StrEnum):
    NS = '│'
    EW = '─'
    NE = '└'
    NW = '┘'
    SW = '┐'
    SE = '┌'
    EMPTY = '·'
    START = 'S'
    OUTSIDE = 'O'
    INSIDE = 'I'

    @memoized
    def directions(self) -> Set[Direction]:
        match self:
            case PipeType.NS:
                result = {Direction.NORTH, Direction.SOUTH}
            case PipeType.EW:
                result = {Direction.EAST, Direction.WEST}
            case PipeType.NE:
                result = {Direction.NORTH, Direction.EAST}
            case PipeType.NW:
                result = {Direction.NORTH, Direction.WEST}
            case PipeType.SW:
                result = {Direction.SOUTH, Direction.WEST}
            case PipeType.SE:
                result = {Direction.SOUTH, Direction.EAST}
            case _:
                result = set()
        return result

    @memoized
    def connects(self, directory: Direction) -> bool:
        match directory:
            case Direction.NORTH:
                return self.connectsNorth()
            case Direction.WEST:
                return self.connectsWest()
            case Direction.EAST:
                return self.connectsEast()
            case Direction.SOUTH:
                return self.connectsSouth()
        raise ValueError(f'unexpected direction: {directory}')

    @memoized
    def connectsNorth(self) -> bool:
        return self in {PipeType.NS, PipeType.NW, PipeType.NE}

    @memoized
    def connectsWest(self) -> bool:
        return self in {PipeType.EW, PipeType.NW, PipeType.SW}

    @memoized
    def connectsEast(self) -> bool:
        return self in {PipeType.EW, PipeType.NE, PipeType.SE}

    @memoized
    def connectsSouth(self) -> bool:
        return self in {PipeType.NS, PipeType.SW, PipeType.SE}

    @staticmethod
    def select(dirs: Set[Direction]) -> PipeType:
        pipeTypes = [t for t in PipeType if t.directions() == dirs]
        if len(pipeTypes) != 1:
            raise ValueError(f'{dirs} failed to match single PipeType: {pipeTypes}')
        return pipeTypes[0]

class Bounds:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def __str__(self) -> str:
        return f'height={self.height} width={self.width}'

    def isWithin(self, x: int, y: int) -> bool:
        return 0 <= x and x < self.width and 0 <= y and y < self.height

class Coordinate:
    def __init__(self, x: int, y:int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinate):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash(repr(self))

class Pipe:
    def __init__(self, pipeType: PipeType, coord: Optional[Coordinate] = None) -> None:
        self.pipeType = pipeType
        self.coord = coord
        self.connections = {}

    def __str__(self) -> str:
        return f'{self.pipeType} {self.coord}'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pipe):
            return False
        return self.pipeType == other.pipeType and self.coord == other.coord

    def __hash__(self) -> int:
        return hash(repr(self))

    def connect(self, direction: Direction, pipe: Pipe):
        self.connections[direction] = pipe

    @staticmethod
    def parseFrom(ch: chr) -> Pipe:
        return Pipe(PipeType(ch))

class Grid:
    def __init__(self, grid: List[List[Pipe]]) -> None:
        if len(grid) == 0 or len(grid[0]) == 0:
            raise ValueError(f'grid is empty: {grid}')
        height = len(grid)
        width = len(grid[0])
        self.bounds = Bounds(height, width)
        for row in grid:
            if len(row) != width:
                raise ValueError(f'grid is uneven: {grid}')
        self.grid = grid
        self.start = self._find(PipeType.START)
        self.pipes = {}
        self._replaceStart()
        self._connectAll()

    def __getitem__(self, coord: Coordinate) -> Pipe:
        if coord is None:
            return None
        return self.grid[coord.y][coord.x]

    def __setitem__(self, coord: Coordinate, pipe: Pipe) -> None:
        self.grid[coord.y][coord.x] = pipe

    def __str__(self) -> str:
        return "\n".join([
            "".join(
                [col.pipeType for col in row]
            )
            for row
            in self.grid
        ])

    def __repr__(self) -> str:
        return self.__str__()

    def _find(self, pipeType: PipeType) -> Coordinate:
        for y in range(self.bounds.height):
            for x in range(self.bounds.width):
                if self.grid[y][x].pipeType == pipeType:
                    return Coordinate(x, y)
        raise ValueError(f'cannot find start: {self.grid}')

    def _replaceStart(self):
        dirs = set()
        for direction in Direction:
            other = self[self.direction(self.start, direction)]
            if not other is None and other.pipeType.connects(direction.opposite()):
                dirs.add(direction)
        t = PipeType.select(dirs)
        self.grid[self.start.y][self.start.x] = Pipe(t, coord=self.start)

    def direction(self, coord: Coordinate, direction: Direction) -> Coordinate:
        match direction:
            case Direction.NORTH:
                return self._northOf(coord)
            case Direction.WEST:
                return self._westOf(coord)
            case Direction.EAST:
                return self._eastOf(coord)
            case Direction.SOUTH:
                return self._southOf(coord)
        raise ValueError(f'unexpected direction: {direction}')

    def _northOf(self, coord: Coordinate) -> Coordinate:
        return self._bound(coord.x, coord.y - 1)

    def _westOf(self, coord: Coordinate) -> Coordinate:
        return self._bound(coord.x - 1, coord.y)

    def _eastOf(self, coord: Coordinate) -> Coordinate:
        return self._bound(coord.x + 1, coord.y)

    def _southOf(self, coord: Coordinate) -> Coordinate:
        return self._bound(coord.x, coord.y + 1)

    def _bound(self, x: int, y: int):
        if not self.bounds.isWithin(x, y):
            return None
        return Coordinate(x, y)

    def _connectsNorth(self, coord: Coordinate):
        return self._hasType(coord, {PipeType.NS, PipeType.NW, PipeType.NE})

    def _connectsWest(self, coord: Coordinate):
        return self._hasType(coord, {PipeType.EW, PipeType.NW, PipeType.SW})

    def _connectsEast(self, coord: Coordinate):
        return self._hasType(coord, {PipeType.EW, PipeType.NE, PipeType.SE})

    def _connectsSouth(self, coord: Coordinate):
        return self._hasType(coord, {PipeType.NS, PipeType.SW, PipeType.SE})

    def _hasType(self, coord: Coordinate, types: Set[PipeType]) -> bool:
        if coord is None:
            return False
        return self[coord].pipeType in types

    def _connectAll(self) -> None:
        for y in range(self.bounds.height):
            for x in range(self.bounds.width):
                self._connect(Coordinate(x, y))

    def _connect(self, coord: Coordinate) -> None:
        pipe = self[coord]
        pipe.coord = coord
        if pipe.pipeType == PipeType.EMPTY:
            return
        self.pipes[coord] = pipe
        for direction in Direction:
            if pipe.pipeType.connects(direction):
                other = self[self.direction(coord, direction)]
                if other is not None and other.pipeType.connects(direction.opposite()):
                    pipe.connect(direction, other)

    def clear(self, coord: Coordinate) -> Pipe:
        old = self[coord]
        self.grid[coord.y][coord.x] = Pipe(PipeType.EMPTY, coord)
        return old

    @staticmethod
    def parseFrom(file: TextIO) -> Grid:
        grid = [
            [Pipe.parseFrom(ch) for ch in line.strip()]
            for line
            in file
        ]
        return Grid(grid)

class Loop:
    def __init__(self, start: Pipe, pipes: Dict[Coordinate, Pipe]) -> None:
        self.start = start
        self.pipes = pipes

    def __str__(self) -> str:
        return str(self.pipes)

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def findIn(grid: Grid) -> Loop:
        pipes = {}
        start = grid[grid.start]
        connected = [start]
        processed = set()
        while len(connected) > 0:
            pipe = connected.pop()
            processed.add(pipe)
            more = set(pipe.connections.values()).difference(processed)
            connected.extend(more)
            pipes[pipe.coord] = pipe
        return Loop(start, pipes)

    def contains(self, coord: Coordinate) -> bool:
        result = coord in set(self.pipes.keys())
        #print(f'{coord} in {set(self.pipes.keys())} = {result}')
        return result

    def clearRemainderOf(self, grid: Grid) -> None:
        coordsToClear = set(grid.pipes.keys()).difference(set(self.pipes))
        for coord in coordsToClear:
            grid.clear(coord)

    def distanceToFarthestPointFromStart(self) -> int:
        return math.ceil(len(self.pipes) / 2)

    def farthestPointFromStart(self) -> Pipe:
        distance = self.distanceToFarthestPointFromStart()
        seen = {self.start}
        a = b = self.start
        for _ in range(distance):
            a = next(iter(set(a.connections.values()).difference(seen)), None)
            if a is not None:
                seen.add(a)
            b = next(iter(set(b.connections.values()).difference(seen)), None)
            if b is not None:
                seen.add(b)
        print(f'a={a} b={b}')
        return b if a is None else a

    def fillInsideAndOutside(self, grid: Grid) -> Dict[PipeType, int]:
        counts = {
            PipeType.INSIDE: 0,
            PipeType.OUTSIDE: 0,
        }
        for y in range(grid.bounds.height):
            inside = False
            south = False
            north = False
            for x in range(grid.bounds.width):
                coord = Coordinate(x, y)
                pipeType = grid[coord].pipeType
                if grid[coord].pipeType == PipeType.EMPTY:
                    pipeType = PipeType.INSIDE if inside else PipeType.OUTSIDE
                    grid[coord] = Pipe(pipeType, coord)
                    counts[pipeType] = counts[pipeType] + 1
                else:
                    dirs = pipeType.directions()
                    if Direction.NORTH in dirs:
                        north = not north
                    if Direction.SOUTH in dirs:
                        south = not south
                    if north and south:
                        inside = not inside
                        north = False
                        south = False
        return counts

grid = Grid.parseFrom(sys.stdin)
print(grid)

loop = Loop.findIn(grid)
print(loop.distanceToFarthestPointFromStart())

loop.clearRemainderOf(grid)
print(grid)

counts = loop.fillInsideAndOutside(grid)
print(grid)

for pipeType, count in counts.items():
    print(f'{pipeType.name}: {count}')
