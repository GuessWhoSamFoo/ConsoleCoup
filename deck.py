import random


class Deck:

    cards = None

    pile = {"Duke": 3,
            "Assassin": 3,
            "Ambassador": 3,
            "Captain": 3,
            "Contessa": 3}

    def __init__(self):
        self.cards = sum(Deck.pile.values()) # Total number of cards

    def draw(self, num_cards):
        self.cards -= num_cards
        valid = False
        counter = 0
        drawn_cards = []
        while not valid or counter < num_cards:
            card_drawn = random.choice(Deck.pile.keys())
            if Deck.pile[card_drawn] > 0:
                Deck.pile[card_drawn] -= 1
                counter += 1
                drawn_cards.append(card_drawn)
                valid = True
        return drawn_cards

if __name__ == '__main__':
    # Testing methods
     print Deck().cards
     print Deck().draw(14)
     print Deck().pile
