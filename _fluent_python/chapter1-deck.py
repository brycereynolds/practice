import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = ['hearts', 'diamonds', 'spades', 'clubs']

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    # 1. The users of your classes don't have to memorize arbitrary method names for standard operations
    # ("How to get the number of items? Is it .size() .length() or what?"")
    # 
    # 2. It's easier to benefit from the rich Python standard library and avoid reinventing the wheel,
    # like the random.choice function.
    def __len__(self):
        return len(self._cards)


    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()

print("len(deck) => {0}".format(len(deck)))

from random import choice
print("choice(deck) => {0}".format(choice(deck)))

print("deck[:3] => {0}".format(deck[:3]))
print("deck[12::13] => {0}".format(deck[12::13]))

print("Card('Q', 'hearts') in deck => {0}".format(Card('Q', 'hearts') in deck))
print("Card('Q', 'beasts') in deck => {0}".format(Card('Q', 'beasts') in deck))

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck[0::13], key=spades_high):
    print(card)
