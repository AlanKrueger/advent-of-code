import re
import sys

cardPattern = re.compile("Card (\d+)")

class Card:
    def __init__(self, num, winning, have):
        self.num = num
        self.winning = winning
        self.have = have
        self.overlap = len(winning & have)
        self.score = 0 if self.overlap == 0 else 2 ** (self.overlap - 1)

    @staticmethod
    def parse(line):
        pieces = line.split(":")
        num = int(pieces[0].split()[1])
        pieces = pieces[1].split("|")
        winning = {int(piece) for piece in pieces[0].split()}
        have = {int(piece) for piece in pieces[1].split()}
        return Card(num, winning, have)

cards = {}
for line in sys.stdin:
    card = Card.parse(line)
    cards[card.num] = card

counts = {}
acc = []
for num in cards.keys():
    counts[num] = 1
for num in sorted(cards.keys()):
    for i in range(len(acc)):
        if acc[i] > 0:
            acc[i] = acc[i] - 1
            counts[num] = counts[num] + 1
    acc = [num for num in acc if num > 0]
    if cards[num].overlap > 0:
        for i in range(counts[num]):
            acc.append(cards[num].overlap)

for num in sorted(cards.keys()):
    print(counts[num])