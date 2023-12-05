import re

debugEnabled = False
def debug(str):
    if debugEnabled:
        print(str)

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'[{self.start},{self.end})'
    
    def __repr__(self):
        return self.__str__()

    def clamp(self, value):
        if isinstance(value, Range):
            return Range(self.clamp(value.start), self.clamp(value.end - 1) + 1)
        return max(self.start, min(value, self.end - 1))

symbolPattern = re.compile("[^.0-9]")

class Symbol:
    def __init__(self, ch, lineIndex, pos):
        self.ch = ch
        self.lineIndex = lineIndex
        self.pos = pos

    def __str__(self):
        return f'\'{self.ch}\' at [{self.lineIndex}, {self.pos}]'
    
    def __repr__(self):
        return self.__str__()
    
    def __hash__(self):
        return hash(self.__members__())

    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        return self.__members__() == other.__members__()

    def __members__(self):
        return (self.ch, self.lineIndex, self.pos)


    @staticmethod
    def findAll(str, lineIndex, range):
        debug(f'Symbol.findAll("{str}", {lineIndex}, {range})')
        str = str[range.start:range.end]
        matches = re.finditer(symbolPattern, str)
        symbols = []
        for match in matches:
            symbols.append(Symbol(match.group(), lineIndex, match.start() + range.start))
        debug(symbols)
        return symbols

class PartNumber:
    def __init__(self, number, symbols):
        self.number = number
        self.symbols = symbols
        
    def __str__(self):
        return f'{self.number}:{self.symbols}'
    
    def __repr__(self):
        return self.__str__()

class Gear:
    def __init__(self, one, two):
        self.one = one
        self.two = two
        
    def __str__(self):
        return f'{self.one}/{self.two}'
    
    def __repr__(self):
        return self.__str__()

    def ratio(self):
        return self.one.number * self.two.number

class Schematic:
    def __init__(self, lines):
        self.lines = lines

    @staticmethod
    def load(stdin):
        lines = [line.strip() for line in stdin]
        return Schematic(lines)
    
    def __str__(self):
        return "\n".join(self.lines)
    
    def __repr__(self):
        return self.__str__()

    def partNumbers(self):
        result = []
        for index, line in enumerate(self.lines):
            debug(f'testing {index}:"{line}"')
            matches = re.finditer("\d+", line)
            for match in matches:
                symbols = self.adjacentSymbols(index, match)
                debug(f'symbols: {symbols}')
                if len(symbols) > 0:
                    result.append(PartNumber(int(match.group()), symbols))
        return result

    def adjacentSymbols(self, index, match):
        debug(f'adjacentSymbols({index}, {match})')
        matchRange = Range(match.start() - 1, match.end() + 1)
        symbols = []

        if index > 0:
            line = self.lines[index - 1]
            range = Range(0, len(line)).clamp(matchRange)
            symbols.extend(Symbol.findAll(line, index - 1, range))
            
        line = self.lines[index]
        range = Range(0, len(line)).clamp(matchRange)
        symbols.extend(Symbol.findAll(line, index, range))
        
        if index + 1 < len(self.lines):
            line = self.lines[index + 1]
            range = Range(0, len(line)).clamp(matchRange)
            symbols.extend(Symbol.findAll(line, index + 1, range))

        return symbols

    def gears(self):
        partSymbolXref = {}
        for part in self.partNumbers():
            for symbol in part.symbols:
                partSymbolXref.setdefault(symbol, []).append(part)
        debug(partSymbolXref)
        results = []
        for symbol in partSymbolXref:
            if symbol.ch == '*':
                parts = partSymbolXref[symbol]
                debug(f'possible gear with parts {parts}')
                if len(parts) == 2:
                    results.append(Gear(parts[0], parts[1]))
        return results