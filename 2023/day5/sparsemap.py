
class Triple:
    def __init__(self, dest, src, len):
        self.dest = dest
        self.src = src
        self.len = len
    
    def __str__(self):
        return f'{self.dest} {self.src} {self.len}'
        
class SparseMap:
    def __init__(self, triples):
        self.triples = sorted(triples, key=lambda t: t.src)

    @staticmethod
    def parseFrom(file):
        triples = []

        values = file.readline().split()
        while len(values) > 0:
            if len(values) != 3:
                raise ValueError(f'expected three map values, got {values}')
            values = [int(value) for value in values]
            triples.append(Triple(dest = values[0], src = values[1], len = values[2]))
            values = file.readline().split()
        
        return SparseMap(triples)
    
    def __str__(self):
        return ", ".join([str(triple) for triple in self.triples])
    
    def __getitem__(self, key):
        triple = self.triple(key)
        #print(f'Found triple {triple} for {key}')
        if triple == None:
            #print(f'mapping {key} to itself')
            return key
        if key < triple.src or triple.src + triple.len <= key:
            raise ValueError("matched triple {triple} appears to be wrong for {key}")
        value = triple.dest + (key - triple.src)
        #print(f'mapping {key} to {value}')
        return value

    def triple(self, key):
        low = 0
        high = len(self.triples) - 1
        while low <= high:
            mid = int((low + high) / 2)
            triple = self.triples[mid]
            if triple.src + triple.len - 1 < key:
                low = mid + 1
            elif key < triple.src:
                high = mid - 1
            else:
                return triple
        return None