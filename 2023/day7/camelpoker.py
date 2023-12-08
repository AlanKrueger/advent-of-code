import sys

class Card:
    def __init__(self, symbol, order):
        self.symbol = symbol
        self.order = order

    @staticmethod
    def withSymbol(symbol):
        return _cardsBySymbol[symbol]
    
    def __str__(self):
        return self.symbol
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return False
        return self.symbol == other.symbol and self.order == other.order
    
    def __hash__(self):
        return hash(repr(self))

    def __lt__(self, other):
        return self.order < other.order

class CardWithCount:
    def __init__(self, card, count):
        self.card = card
        self.count = count

    def __str__(self):
        return f'{self.card}:{self.count}'
    
    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        if self.count > other.count:
            return True
        if self.count < other.count:
            return False
        return self.card < other.card


_cardSymbols = 'AKQJT98765432'
_cards = [Card(symbol, i) for i, symbol in enumerate(_cardSymbols)]

_cardsBySymbol = {}
for card in _cards:
    _cardsBySymbol[card.symbol] = card

class Hand:
    def __init__(self, cards, bid):
        counts = {}
        for card in cards:
            counts[card] = counts.get(card, 0) + 1
        self.cards = cards
        self.bid = bid
        self.cardCounts = counts
        self.handType = next(filter(lambda type: type.matches(self), _handTypes))

    @staticmethod
    def parseFrom(line):
        pieces = line.split()
        symbols = pieces[0]
        bid = int(pieces[1])
        cards = [Card.withSymbol(symbol) for symbol in symbols]
        return Hand(cards, bid)
    
    def __str__(self):
        return "".join([card.symbol for card in self.cards])
    
    def __repr__(self):
        return self.__str__()
    
    def __lt__(self, other):
        if self.handType < other.handType:
            return True
        if self.handType > other.handType:
            return False
        for i in range(len(self.cards)):
            if self.cards[i] < other.cards[i]:
                return True
            if self.cards[i] > other.cards[i]:
                return False
        return False

class HandType:
    def order(self):
        pass
    def matches(self, hand):
        pass
    def __str__(self):
        return self.__class__.__name__
    def __eq__(self, other):
        if not isinstance(other, HandType):
            return False
        return self.order() == other.order()
    def __lt__(self, other):
        return self.order() < other.order()

class FiveOfAKind(HandType):
    def order(self):
        return 0
    def matches(self, hand):
        return 5 in hand.cardCounts.values()
    
class FourOfAKind(HandType):
    def order(self):
        return 1
    def matches(self, hand):
        return 4 in hand.cardCounts.values()
    
class FullHouse(HandType):
    def order(self):
        return 2
    def matches(self, hand):
        return 3 in hand.cardCounts.values() and 2 in hand.cardCounts.values()
    
class ThreeOfAKind(HandType):
    def order(self):
        return 3
    def matches(self, hand):
        return 3 in hand.cardCounts.values()
    
class TwoPair(HandType):
    def order(self):
        return 4
    def matches(self, hand):
        pairs = [count for count in hand.cardCounts.values() if count == 2]
        return len(pairs) == 2

class OnePair(HandType):
    def order(self):
        return 5
    def matches(self, hand):
        pairs = [count for count in hand.cardCounts.values() if count == 2]
        return len(pairs) == 1
    
class HighCard(HandType):
    def order(self):
        return 6
    def matches(self, hand):
        return True
    
_handTypes = [FiveOfAKind(), FourOfAKind(), FullHouse(), ThreeOfAKind(), TwoPair(), OnePair(), HighCard()]

hands = [Hand.parseFrom(line) for line in sys.stdin]
hands.sort(reverse=True)

sum = 0
for i in range(len(hands)):
    rank = i + 1
    hand = hands[i]
    print(f'{hand.handType} {hand.cards} = {hand.bid} * {rank}')
    sum = sum + rank * hands[i].bid
print(sum)