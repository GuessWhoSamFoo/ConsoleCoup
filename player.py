from deck import *


class Player:

    def __init__(self, turn, coins, influence):
        self.turn = turn
        self.coins = coins
        self.influence = influence # Influence object is a list of up to two characters

    def income(self):
        self.coins += 1

    def foreign_aid(self):
        self.coins += 2

    def coup(self):
        if self.coins >= 7:
            self.coins -= 7
        else:
            print "Not enough coins!"
        # Decide how to make another player lose influence
        player_num = int(raw_input("Choose player number to lose influence: "))
        player[player_num].influence.pop()

    def tax(self):
        self.coins += 3

    def assassinate(self):
        if self.coins >= 3:
            self.coins -= 3
        else:
            print "Not enough coins!"

    def exchange(self):
        # Pick from own influence
        inf_name = raw_input("Select influence to exchange: ")
        while inf_name not in self.influence:
            print "You don't have that card!"
            print self.influence
            inf_name = raw_input("Try again: ")
        available_cards = Deck().draw(2) + [inf_name]

        # Draw two cards from deck and keep one of three
        select_card = raw_input("Please swap " + inf_name + " for " + str(available_cards) + ": ")
        while select_card not in available_cards:
            select_card = raw_input("Enter a valid option: ")
        self.influence[self.influence.index(inf_name)] = select_card
        available_cards.remove(select_card)

        # Replace unselected cards in deck
        for card in available_cards:
            Deck().pile[card] += 1

    def steal(self, target_player):
        self.coins += 2
        target_player.coin -= 2
        # Another player loses two coins

    def block(self):
        if not self.turn:
            return

# Initialize new game, always starts player 1
player_1 = Player(True, 2, Deck().draw(2))
player_2 = Player(False, 2, Deck().draw(2))
player_3 = Player(False, 2, Deck().draw(2))
player_4 = Player(False, 2, Deck().draw(2))

player = [player_1, player_2, player_3, player_4]

if __name__ == '__main__':
    Player(False, 2, [Deck().draw(2)])
    print Player.influence

