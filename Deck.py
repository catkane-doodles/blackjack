from Card import Card
from random import shuffle


class Deck:
    def __init__(self, deckSize):
        self.cards = []
        suits = ['D', 'C', 'H', 'S']
        face = list(range(1, 11)) + ['J', 'Q', 'K']
        for x in range(deckSize):
            for suit in suits:
                for i in range(13):
                    card = str(face[i]) + suit
                    self.cards.append(Card(card, min(i + 1, 10)))

            shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)

    def deckSize(self):
        return len(self.cards)
