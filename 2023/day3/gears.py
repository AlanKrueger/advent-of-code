import sys
from schema import *

schematic = Schematic.load(sys.stdin)
for gear in schematic.gears():
    print(gear.ratio())