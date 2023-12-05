import sys
from schema import *

schematic = Schematic.load(sys.stdin)
for part in schematic.partNumbers():
    print(part.number)