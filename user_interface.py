import os


class UI:
    def __init__(self, something):
        self.something = something

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def players(player1, player2, player3, player4):
        print "Player 1 (You)" + str(player1.influence)
        print "Player 2 " + str(player2.influence)
        print "Player 3 " + str(player3.influence)
        print "Player 4 " + str(player4.influence)

    @staticmethod
    def action_menu():
        print "|  Character  |     Action      |      Effect                                  |     Counteraction    |"
        print "|   -------   | 1 - Income      | Take 1 coin                                  |           X          |"
        print "|   -------   | 2 - Foreign Aid | Take 2 coins                                 |           X          |"
        print "|   -------   | 3 - Coup        | Pay 7 coins / Chose player to lose influence |           X          |"
        print "|    Duke     | 4 - Tax         | Take 3 coins                                 | Blocks Foreign Aid   |"
        print "|  Assassin   | 5 - Assassinate | Pay 3 coins / Chose player to lose influence |           X          |"
        print "|  Ambassador | 6 - Exchange    | Exchange cards with deck                     | Blocks Stealing      |"
        print "|  Captain    | 7 - Steal       | Take 2 coins form another player             | Blocks Stealing      |"
        print "|  Contessa   |     -------     | -----------                                  | Blocks Assassination |"


def actions(player_taking_action, num):
    if num == 1:
        return player_taking_action.income()
    elif num == 2:
        return player_taking_action.foreign_aid()
    elif num == 3:
        return player_taking_action.coup()
    elif num == 4:
        return player_taking_action.tax()
    elif num == 5:
        return player_taking_action.assassinate()
    elif num == 6:
        return player_taking_action.exchange()
    elif num == 7:
        return player_taking_action.steal()


