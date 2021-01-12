class Player():
    def __init__(self):
        self.hand = []
        self.value = 0

        self.minimum = 13

    def calculateValue(self):
        self.value = 0

        # Sorting cards, add the biggest first so that the value of A can be determined
        tmp = sorted(self.hand, key=lambda x: x.value, reverse=True)

        # Counting value of card

        # Edge case of 2 aces
        if len(tmp) == 2:
            if tmp[0].value == 1 and tmp[1].value == 1:
                self.value = 21
                return

        for card in tmp:
            if card.value == 1:
                if self.value + card.value > 21:
                    self.value += 1
                else:
                    self.value += 11
            else:
                self.value += card.value

    def logic(self):
        return self.value < self.minimum and len(self.hand) < 5

    def draw(self, card):
        self.hand.append(card)

    def reset(self):
        self.hand = []
        self.value = 0
