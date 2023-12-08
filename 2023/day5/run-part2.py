import sys
from almanac import *
from alive_progress import alive_bar

almanac = Almanac.parseFrom(sys.stdin, seedRanges=True)

minLocation = None
totalSeeds = sum([seedRange.len for seedRange in almanac.seeds])
with alive_bar(totalSeeds) as bar:
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
            bar()

print(minLocation)