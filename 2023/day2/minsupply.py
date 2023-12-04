import sys
from game import *

for line in sys.stdin:
    game = Game.parse(line)
    print(game.minSupply().power())
