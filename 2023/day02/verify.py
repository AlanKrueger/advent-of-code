import sys
from game import *

supply = Sample(red = 12, green = 13, blue = 14)

for line in sys.stdin:
    game = Game.parse(line)
    if game.possibleWith(supply):
        print(game.num)
