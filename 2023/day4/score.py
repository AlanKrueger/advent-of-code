import re
import sys

cardPattern = re.compile("Card (\d+)")

class Card:
    def __init__(self, number, winning, have):
        self.number = number
        self.winning = winning
        self.have = have
        overlap = len(winning & have)
        self.score = 0 if overlap == 0 else 2 ** (overlap - 1)

    @staticmethod
    def parse(line):
        pieces = line.split(":")
        number = int(pieces[0].split()[1])
        pieces = pieces[1].split("|")
        winning = {piece for piece in pieces[0].split()}
        have = {piece for piece in pieces[1].split()}
        return Card(number, winning, have)

for line in sys.stdin:
    card = Card.parse(line)
    print(card.score)