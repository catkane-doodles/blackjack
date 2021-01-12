class CardCounter():
    def __init__(self):
        self.count = 0

    def countCard(self, card):
        if 2 <= card.value and card.value <= 6:
            self.count += 1
            state = "+1"
        elif card.value == 1 or card.value == 10:
            self.count -= 1
            state = "-1"
        else:
            state = "+0"

        # print(card.value, state)
