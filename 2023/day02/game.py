import functools
import re

class Sample:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f'{self.red} red, {self.green} green, {self.blue} blue'

    @staticmethod
    def parse(str):
        counts = {"red": 0, "green": 0, "blue": 0}
        pieces = re.split("\s*,\s*", str)
        for piece in pieces:
            parts = re.split("\s+", piece)
            counts[parts[1]] = int(parts[0])
        return Sample(counts["red"], counts["green"], counts["blue"])
    
    def possibleWith(self, supply):
        return (
            self.red <= supply.red
            and self.green <= supply.green
            and self.blue <= supply.blue
        )
    
    @staticmethod
    def max(a, b):
        return Sample(
            red = max(a.red, b.red),
            green = max(a.green, b.green),
            blue = max(a.blue, b.blue),
        )
    
    def power(self):
        return self.red * self.green * self.blue

class Game:
    def __init__(self, num, samples):
        self.num = num
        self.samples = samples
    
    def __str__(self):
        return f'Game {self.num}: {"; ".join(map(lambda s : str(s), self.samples))}'

    @staticmethod
    def parse(line):
        # Game <#>: <sample> [; <sample>]*
        pieces = re.split("\s*:\s*", line)
        num = int(re.search("\d+", pieces[0]).group())
        samples = map(Sample.parse, re.split("\s*;\s*", pieces[1]))
        return Game(num, samples)
    
    def possibleWith(self, supply):
        for sample in self.samples:
            if not sample.possibleWith(supply):
                return False
        return True
    
    def minSupply(self):
        return functools.reduce(Sample.max, self.samples)
