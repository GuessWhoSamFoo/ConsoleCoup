from user_interface import *
from player import *
from deck import *

# Initial setup code to display UI
UI.cls()  # Clears the console
UI.players(player_1, player_2, player_3, player_4)
UI.action_menu()


def state_of_game():
    print "Your coins: " + str(player_1.coins)
    print "Player 2: " + str(player_2.coins)
    print "Player 3: " + str(player_3.coins)
    print "Player 4: " + str(player_4.coins)
    print Deck().pile

while len(player) > 1:

    while player_1.turn:
        if player_1.coins >= 10:
            actions(player_1, 3)
        else:
            actions(player_1, int(raw_input("Action: ")))

        player_1.turn = False

    actions(player_2, 1)
    actions(player_3, 1)
    actions(player_4, 1)
    break
