from Deck import Deck
from Player import Player
from Dealer import Dealer
from CardCounter import CardCounter


class Engine():
    def __init__(self, playerCount, deckSize):
        self.deck = Deck(deckSize)
        self.players = [Player()
                        for i in range(playerCount)]

        # Adding Dealer to players
        self.players += [Dealer()]

        self.cardCounter = CardCounter()

    def setupGame(self):
        for i in range(2):
            for p in self.players:
                card = self.deck.deal()
                if i == 1:
                    self.cardCounter.countCard(card)
                p.draw(card)

    def playerName(self, p):
        if type(p) == Dealer:
            return "Dealer "
        return "Player " + str(self.players.index(p) + 1)

    def checkWinState(self):
        p = self.players[-1]
        p.calculateValue()
        dealerValue = p.value
        print("{0} \t\t({1}, {2} cards, {3})".format(
            self.playerName(p), p.value, len(p.hand), list(card.value for card in p.hand)))

        for p in self.players[:-1]:
            p.calculateValue()

            winState = None

            if dealerValue > 21:
                if p.value > 21:
                    winState = "draws"
                else:
                    winState = "wins"
            else:
                if p.value > dealerValue and p.value <= 21:
                    winState = "wins"
                elif p.value == dealerValue:
                    winState = "draws"
                else:
                    winState = "loses"

            print("{0} {1}\t({2}, {3} cards, {4})".format(
                self.playerName(p), winState, p.value, len(p.hand), list(card.value for card in p.hand)))

    def run(self):
        self.setupGame()

        for p in self.players:
            p.calculateValue()
            while p.logic():
                card = self.deck.deal()
                self.cardCounter.countCard(card)
                p.draw(card)
                p.calculateValue()

        print()
        self.checkWinState()
        print("Card count: {0}".format(self.cardCounter.count), end="\n\n")

    def reset(self):
        for p in self.players:
            p.reset()


engine = Engine(3, 6)
for x in range(30):
    print("Round {0}".format(x+1))
    engine.run()
    engine.reset()
