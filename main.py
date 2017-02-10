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
    print player_1.influence
    print player_2.influence
    print player_3.influence
    print player_4.influence
    print Deck().pile

while len(player) > 1:

    while player_1.turn:
        valid_move = False
        if player_1.coins >= 10: # Must coup if 10+ coins
            actions(player_1, 3)
        else:
            while not valid_move:
                valid_move = actions(player_1, int(raw_input("Action: ")))
        player_1.turn = False

    actions(player_2, 1)
    actions(player_3, 1)
    actions(player_4, 1)

    UI.action_menu() # Reprint menu each new round
    state_of_game()
    player_1.turn = True


