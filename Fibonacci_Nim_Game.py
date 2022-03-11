# CS112
# Fibbonacci nim game
# done by hazem walied
# 27/2/2022
# version 1.0

##################################################
turns = 0
previous_action = 0


def get_n_coins():                 # this function is used to get the number of coins to start the game with
    global n_coins
    is_valid = False
    while not is_valid:
        n_coins = input("Please enter the number of coins to start th game with (AT LEAST 3): ")
        is_valid = n_coins.isdigit() and int(n_coins)>2
    return n_coins


def display_board(n_coins):        # this function is used to display the game board only for the first time
    print("THE NUMBER OF COINS IS: ", n_coins)


def get_input(player):             # used to get the number of coins to remove and print messages if input is npt valid
    global previous_action
    global action
    valid = False
    while not valid :
        action = input("[PLAYER "+player+"] Please enter the number of coins you want to remove: ")
        if action.isdigit():
            if int(action)>0:
                valid = True
            else:
                print("number can’t be negative please enter a positive one ")
            if turns == 0:
                if int(action) > int(n_coins):
                    print("number of coins can’t be equal to total number")
                elif int(action) > 3:
                    print("you can’t enter a number greater than 2 in the first turn ")
                else:
                    Valid = True
            else:
                if int(action) > (2 * int(previous_action)) :
                    print("number can’t be greater than double of the previous turn")
                elif (int(n_coins)-int(action))<0:
                    print("No enough coins to make that move")
                else:
                    Valid = True
        else:
            print("Invalid input please enter a positive integer number ")
        return action


def valid_action(action):     # this function decides if the move is valid or not to decide to update the numbers or not
    global previous_action
    valid1 = False
    while not valid1:
        if action.isdigit():
            if int(action) > 0:
                valid1 = True
            else:
                valid1 = False
            if turns == 0:
                if int(action) > int(n_coins):
                    valid1 = False
                elif int(action) > 3:
                    valid1 = False
                else:
                    valid1 = True
            else:
                if int(action) > (2 * int(previous_action)) :
                    valid1 = False
                elif (int(n_coins)-int(action))<0:
                    valid1 = False
                else:
                    valid1 = True
        else:
            valid1 = False
        return valid1


def update_game(action):            # this function is used to update the game state if the numbers are valid
    global previous_action
    global n_coins
    if valid_action(action):
        n_coins = int(n_coins)
        n_coins -= int(action)
        print("THE NUMBER OF COINS REMAINING IS: " + str(n_coins))
        previous_action = action
    else:
        print("THE NUMBER OF COINS REMAINING IS: " + str(n_coins))


def is_winner():                    # this function checks if player is winner
    global n_coins
    cond = False
    if int(n_coins)<= 1:
        cond = True
    return cond


def play_again():                   # this function asks the users if they want to play again after the game has ended
    if is_winner():
        print("------------------------------------------")
        key = input("    PRESS ANY KEY TO PLAY AGAIN     \n                 OR\n       PRESS [Q] TO QUIT GAME\n------------------------------------------")
        if key.lower()!="q":
            again = True
        else:
            again = False
    return again




def play_nim_game():                # finally this is the game function [ENJOY]
    global turns
    global previous_action
    get_n_coins()
    display_board(n_coins)
    while True:
        if is_winner():
            print("********************")
            print("PLAYER 1 WINS")
            print("********************")
            print("GAME ENDED")
            print("********************")
            if play_again()==False:
                break
            else:
                play_nim_game()
        get_input("1")
        update_game(action)
        turns+=1
        if is_winner():
            print("********************")
            print("PLAYER 2 WINS")
            print("********************")
            print("GAME ENDED")
            print("********************")
            if play_again() == False:
                break
            else:
                play_nim_game()
        get_input("2")
        update_game(action)

#######################


play_nim_game()


