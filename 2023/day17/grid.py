# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name, too-few-public-methods, redefined-builtin

from __future__ import annotations
import argparse
import sys
from typing import List
from typing import TextIO
from enum import Enum

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

    def __str__(self) -> str:
        return super().__str__().split('.')[1][0]

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

class Node:
    def __init__(self, coord: Coordinate, loss: int) -> None:
        self.coord = coord
        self.loss = loss
        self.adjacent = {}
        self.weight = None
        self.prev = (None, None)

    def sequential(self, dir: Direction) -> int:
        # if self.coord == Coordinate(0, 3):
        #     print('vvvvvvvvvv')
        # print(f'sequential({self}, {dir})')
        prev, node = self.prev
        # print(f'prev={prev} node={node}')
        count = 0
        if prev == dir:
            count = 1
            if node is not None:
                # print(f'recursing into {node}')
                count += node.sequential(dir)
        # else:
        #     print(f'prev != dir ({prev} != {dir})')
        # print(f'sequential({self}, {dir}) -> {count}')
        # if self.coord == Coordinate(0, 3):
        #     print('^^^^^^^^^^')
        return count

    def __str__(self) -> str:
        return f'{self.coord}'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return False
        return repr(self) == repr(other)

    def __hash__(self) -> int:
        return hash(repr(self))

class Grid:
    def __init__(self, loss: List[List[int]]) -> None:
        self.rows = len(loss)
        self.cols = len(loss[0])
        if not all(len(row) == self.cols for row in loss):
            raise ValueError('Grid must be rectangular')
        self.loss = loss

    def inbounds(self, coord: Coordinate) -> bool:
        return 0 <= coord.row < self.rows and 0 <= coord.col < self.cols

    def minloss(self, src: Coordinate, dst: Coordinate) -> List[Direction]:
        unvisited = [
            Node(Coordinate(row, col), self.loss[row][col])
            for row in range(self.rows)
            for col in range(self.cols)
        ]
        nodes = {node.coord: node for node in unvisited}
        for row in range(self.rows):
            for col in range(self.cols):
                coord = Coordinate(row, col)
                node = nodes[coord]
                for dir in Direction:
                    neighbor = dir.next(coord)
                    if self.inbounds(neighbor):
                        neighborNode = nodes[neighbor]
                        node.adjacent[dir] = neighborNode
        nodes[src].weight = self.loss[src.row][src.col]
        unvisited.sort(key=lambda node: (node.weight is None, node.weight))
        while len(unvisited) > 0:
            u = unvisited.pop(0)
            print(f'visiting {u} weight={u.weight}')
            # if u.coord == dst:
            #     break
            for dir in u.adjacent:
                v = u.adjacent[dir]
                print(f'considering {v} loss={v.loss} weight={v.weight}')
                if v in unvisited:
                    if u.sequential(dir.reverse()) < 3:
                        alt = u.weight + v.loss
                        print(f'alt={alt}')
                        if v.weight is None or alt < v.weight:
                            v.weight = alt
                            v.prev = (dir.reverse(), u)
                            print(f'setting prev of {v} to {v.prev}')
                            t = v.prev[1]
                            while t is not None:
                                print(f'  and prev of {t} is {t.prev}')
                                t = t.prev[1]
                else:
                    print(f'{v} already visited')
            unvisited.sort(key=lambda node: (node.weight is None, node.weight))

        for row in range(self.rows):
            print([nodes[Coordinate(row, col)].weight for col in range(self.cols)])
        print()

        display = [[str(v) for v in row] for row in self.loss]
        node = nodes[dst]
        weight = node.weight
        while node.coord != src:
            prev, next = node.prev
            display[node.coord.row][node.coord.col] = prev.reverse().glyph()
            node = next
        for row in display:
            print(''.join(row))
        print()
        return weight

    @staticmethod
    def parsefrom(file: TextIO) -> Grid:
        content = []
        for line in file:
            content.append([int(ch) for ch in line.strip()])
        return Grid(content)

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
parser.add_argument('--part2', action='store_true')
parser.set_defaults(debug=False, part2=False)
args = parser.parse_args()

grid = Grid.parsefrom(sys.stdin)

if args.debug:
    for row in grid.loss:
        print(''.join(str(fixture) for fixture in row))
    print()

src = Coordinate(0, 0)
dst = Coordinate(grid.rows - 1, grid.cols - 1)
print(grid.minloss(src, dst))
