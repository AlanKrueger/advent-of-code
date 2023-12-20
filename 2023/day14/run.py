# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, redefined-outer-name, non-ascii-name, too-few-public-methods, method-cache-max-size-none

from __future__ import annotations
import argparse
import sys
from typing import List
from typing import TextIO
from functools import cache as memoized
from strenum import StrEnum

class Content(StrEnum):
    EMPTY = '.'
    SQUARE = '#'
    ROUND = 'O'

class Grid:
    def __init__(self, content: List[List[Content]]) -> None:
        self.rows = len(content)
        self.cols = len(content[0])
        self._content = content
        if not all(len(row) == self.cols for row in content):
            raise ValueError(f'grid is not rectangular: {content}')

    def __getitem__(self, row: int) -> List[Content]:
        return self._content[row]

    @memoized
    def tip_north(self) -> Grid:
        content = [list(row) for row in self._content]
        for col in range(self.cols):
            first_empty = None
            for row in range(self.rows):
                c = content[row][col]
                if c == Content.SQUARE:
                    first_empty = None
                if c == Content.EMPTY:
                    first_empty = row if first_empty is None else first_empty
                elif c == Content.ROUND:
                    if first_empty is not None:
                        temp = content[first_empty][col]
                        content[first_empty][col] = content[row][col]
                        content[row][col] = temp
                        first_empty += 1
        newgrid = Grid(content)
        if args.debug:
            print("tip north:")
            print(newgrid)
            print()
        return newgrid

    @memoized
    def tip_west(self) -> Grid:
        content = [list(row) for row in self._content]
        for row in range(self.rows):
            first_empty = None
            for col in range(self.cols):
                c = content[row][col]
                if c == Content.SQUARE:
                    first_empty = None
                if c == Content.EMPTY:
                    first_empty = col if first_empty is None else first_empty
                elif c == Content.ROUND:
                    if first_empty is not None:
                        temp = content[row][first_empty]
                        content[row][first_empty] = content[row][col]
                        content[row][col] = temp
                        first_empty += 1
        newgrid = Grid(content)
        if args.debug:
            print("tip west:")
            print(newgrid)
            print()
        return newgrid
    
    @memoized
    def tip_south(self) -> Grid:
        content = [list(row) for row in self._content]
        for col in range(self.cols):
            first_empty = None
            for row in reversed(range(self.rows)):
                c = content[row][col]
                if c == Content.SQUARE:
                    first_empty = None
                if c == Content.EMPTY:
                    first_empty = row if first_empty is None else first_empty
                elif c == Content.ROUND:
                    if first_empty is not None:
                        temp = content[first_empty][col]
                        content[first_empty][col] = content[row][col]
                        content[row][col] = temp
                        first_empty -= 1
        newgrid = Grid(content)
        if args.debug:
            print("tip south:")
            print(newgrid)
            print()
        return newgrid
    
    @memoized
    def tip_east(self) -> Grid:
        content = [list(row) for row in self._content]
        for row in range(self.rows):
            first_empty = None
            for col in reversed(range(self.cols)):
                c = content[row][col]
                if c == Content.SQUARE:
                    first_empty = None
                if c == Content.EMPTY:
                    first_empty = col if first_empty is None else first_empty
                elif c == Content.ROUND:
                    if first_empty is not None:
                        temp = content[row][first_empty]
                        content[row][first_empty] = content[row][col]
                        content[row][col] = temp
                        first_empty -= 1
        newgrid = Grid(content)
        if args.debug:
            print("tip east:")
            print(newgrid)
            print()
        return newgrid

    @memoized
    def cycle(self) -> Grid:
        return self.tip_north().tip_west().tip_south().tip_east()

    def multicycle(self, n: int) -> Grid:
        result = self
        for _ in range(n):
            result = result.cycle()
        return result

    def load(self) -> int:
        total = 0
        for col in range(self.cols):
            for row in range(self.rows):
                if self[row][col] == Content.ROUND:
                    total += self.rows - row
        return total

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
    def parsefrom(file: TextIO) -> Grid:
        content = []
        for line in file:
            line = line.strip()
            if line == '':
                break
            content.append([Content(c) for c in line])
        return Grid(content)

def floyd(f, x0) -> (int, int):
    """Floyd's cycle detection algorithm."""
    # Main phase of algorithm: finding a repetition x_i = x_2i.
    # The hare moves twice as quickly as the tortoise and
    # the distance between them increases by 1 at each step.
    # Eventually they will both be inside the cycle and then,
    # at some point, the distance between them will be
    # divisible by the period λ.
    tortoise = f(x0) # f(x0) is the element/node next to x0.
    hare = f(f(x0))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))

    # At this point the tortoise position, ν, which is also equal
    # to the distance between hare and tortoise, is divisible by
    # the period λ. So hare moving in cycle one step at a time, 
    # and tortoise (reset to x0) moving towards the cycle, will 
    # intersect at the beginning of the cycle. Because the 
    # distance between them is constant at 2ν, a multiple of λ,
    # they will agree as soon as the tortoise reaches index μ.

    # Find the position μ of first repetition.    
    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)   # Hare and tortoise move at same speed
        mu += 1

    # Find the length of the shortest cycle starting from x_μ
    # The hare moves one step at a time while tortoise is still.
    # lam is incremented until λ is found.
    lam = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lam += 1

    return lam, mu

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
parser.add_argument('--part2', action='store_true')
parser.add_argument('--cycles', type=int, default=1, help='number of cycles to run')
parser.set_defaults(debug=False, part2=False)
args = parser.parse_args()

grid = Grid.parsefrom(sys.stdin)
if args.debug:
    print("grid:")
    print(grid)
    print()

if args.part2:
    (lam, mu) = floyd(lambda g: g.cycle(), grid)
    if args.debug:
        print(f'λ={lam}, μ={mu}')
    if args.cycles < lam + mu:
        for _ in range(args.cycles):
            grid = grid.cycle()
    else:
        for _ in range(mu):
            grid = grid.cycle()
        for _ in range((args.cycles - mu) % lam):
            grid = grid.cycle()
else:
    grid.tip_north()

print(grid.load())
