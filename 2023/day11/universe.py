# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name

from __future__ import annotations

import sys

from typing import List
from typing import Set
from typing import TextIO

class Coordinate:
    def __init__(self, x: int, y: int) -> None:
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
    
    def __lt__(self, other: Coordinate) -> bool:
        if self.y < other.y:
            return True
        if self.y > other.y:
            return False
        if self.x < other.x:
            return True
        return False

    def expand(self, by: int, missingRows: Set[int], missingCols: Set[int]) -> Coordinate:
        toAdd = by - 1
        expandX = 0
        expandY = 0
        for x in range(self.x):
            if x in missingCols:
                expandX += toAdd
        for y in range(self.y):
            if y in missingRows:
                expandY += toAdd
        return Coordinate(self.x + expandX, self.y + expandY)

class CoordinatePair:
    def __init__(self, a: Coordinate, b: Coordinate) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f'{self.a} to {self.b}'
    
    def shortestPathLength(self) -> int:
        return abs(self.a.x - self.b.x) + abs(self.a.y - self.b.y)

class Universe:
    def __init__(self, bound: Coordinate, galaxies: List[Coordinate]) -> None:
        self.bound = bound
        self.galaxies = list(galaxies)
        self.galaxies.sort()

    def __str__(self):
        lines = []
        for y in range(self.bound.y):
            line = []
            for x in range(self.bound.x):
                line.append("#" if Coordinate(x, y) in self.galaxies else ".")
            lines.append("".join(line))
        return "\n".join(lines)

    def expand(self, by: int) -> Universe:
        rows = set()
        cols = set()
        for galaxy in self.galaxies:
            rows.add(galaxy.y)
            cols.add(galaxy.x)
        missingRows = set(range(self.bound.y)) - rows
        missingCols = set(range(self.bound.x)) - cols
        expanded = []
        for galaxy in self.galaxies:
            expanded.append(galaxy.expand(by = by, missingRows = missingRows, missingCols = missingCols))
        bound = self.bound.expand(by = by, missingRows = missingRows, missingCols = missingCols)
        return Universe(bound, expanded)
    
    def galaxyPairs(self) -> List[CoordinatePair]:
        for i, ig in enumerate(self.galaxies):
            for j in range(i + 1, len(self.galaxies)):
                yield CoordinatePair(ig, self.galaxies[j])
    
    @staticmethod
    def parseFrom(file: TextIO) -> Universe:
        galaxies = []
        mx = my = 0
        for y, line in enumerate(file):
            my = max(my, y)
            for x, ch in enumerate(line.strip()):
                mx = max(mx, x)
                if ch == '#':
                    galaxies.append(Coordinate(x, y))
        return Universe(galaxies = galaxies, bound = Coordinate(mx + 1, my + 1))

universe = Universe.parseFrom(sys.stdin)
#print(universe)

universe = universe.expand(1000000)
#print(universe)

total = 0
for pair in universe.galaxyPairs():
    #print(f'{pair}: {pair.shortestPathLength()}')
    total += pair.shortestPathLength()
print(f'total: {total}')
