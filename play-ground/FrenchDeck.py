import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


my_card = Card('7', 'diamonds')
print "Show my card", my_card

deck = FrenchDeck()
print "Length of deck", len(deck)
print "First card", deck[0]
print "Last card", deck[-1]

print "Random Card", choice(deck)
print "Another", choice(deck)