from sparsemap import *

def expect(value, compare):
    if value != compare:
        raise ValueError(f'expecting "{compare}", got "{value}"')
    
class Range:
    def __init__(self, start, len):
        self.start = start
        self.len = len

class Almanac:
    def __init__(self, seeds, maps):
        self.seeds = seeds
        self.maps = maps

    @staticmethod
    def parseFrom(file, seedRanges = False):
        seeds = file.readline().split()
        expect(seeds[0], "seeds:")
        seeds = [int(value) for value in seeds[1:]]
        if seedRanges:
            seeds = [Range(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
        else:
            seeds = [Range(seed, 1) for seed in seeds]
        
        blank = file.readline().strip()
        expect(blank, "")

        maps = {}
        header = file.readline()
        while header != "":
            pieces = header.split()
            expect(pieces[1], "map:")
            name = pieces[0]
            maps[name] = SparseMap.parseFrom(file)
            header = file.readline()
        
        return Almanac(seeds, maps)
    
    def lookup(self, map, key):
        #print(f'looking up {key} in {map}')
        map = self.maps[map]
        #print(f'map is {map}')
        return map[key]
    
    def soilFor(self, seed):
        return self.lookup('seed-to-soil', seed)
    
    def fertilizerFor(self, soil):
        return self.lookup('soil-to-fertilizer', soil)
    
    def waterFor(self, fertilizer):
        return self.lookup('fertilizer-to-water', fertilizer)
    
    def lightFor(self, water):
        return self.lookup('water-to-light', water)
    
    def temperatureFor(self, light):
        return self.lookup('light-to-temperature', light)
    
    def humitityFor(self, temperature):
        return self.lookup('temperature-to-humidity', temperature)
    
    def locationFor(self, humidity):
        return self.lookup('humidity-to-location', humidity)
