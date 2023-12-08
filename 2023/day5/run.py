import sys
from almanac import *

almanac = Almanac.parseFrom(sys.stdin)

minLocation = None
for seedRange in almanac.seeds:
    for seed in range(seedRange.start, seedRange.start + seedRange.len):
        soil = almanac.soilFor(seed)
        fertilizer = almanac.fertilizerFor(soil)
        water = almanac.waterFor(fertilizer)
        light = almanac.lightFor(water)
        temperature = almanac.temperatureFor(light)
        humidity = almanac.humitityFor(temperature)
        location = almanac.locationFor(humidity)
        minLocation = location if minLocation == None else min(minLocation, location)

print(minLocation)