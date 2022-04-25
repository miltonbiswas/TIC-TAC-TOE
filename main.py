# This is Tac-Tac-Toe game.
#The author is Milton Biswas.

#Functions to be print on Tic Tac Toe Board
from ast import Try
from locale import currency
from multiprocessing.sharedctypes import Value
from optparse import Option, Values
from re import X
from secrets import choice
from tabnanny import check
from traceback import print_tb
from winsound import PlaySound


def print_tic_t_t(values):
    print("\n")
    print("\t      |      |")
    print("\t      {}      |      {}").format(values[0], values[1], values[2])
    print('\t______|______|______')

    print("\t      |      |")
    print("\t      {}      |      {}     |      {}".format(values[3], values[4], values[5]))
    print('\t______|______|______')

    print("\t      |      |")

    print("\t   {}   |   {}   |   {}".format(values[6], values[7], values[8]))
    print("\t      |      |")
    print("\n")

# Functions to print the score-board for the game

def print_scoreboard(score_board):
    print("\t-------------------------------------------")
    print("\t      SCOREBOARD FOR TIC TAC TOE           ")
    print("\t-------------------------------------------")

    players = list(score_board.key())
    print("\t     ", players[0], "\t    ",   score_board[players[0]])
    print("\t     ", players[1], "\t    ",   score_board[players[1]])

    print("\t------------------------------------------\n")

#Functions to check if any player has won the game
def check_winner(player_position, current_player):

    #All possible winning comination for the players
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    #Loop to check if any winning combination is setisfied or not
    for x in soln:
        if all(y in player_position[current_player] for y in x):

            #Return True is any winning combination satisfies in the iteration
            return True
        # Return true if any winning combinaton is saisfied or not
        for x in soln:
            if all(y in player_position[current_player] for y in X):
                return False
#Function for single Tic Tac Toe Game
def check_draw(player_position):
    if len(player_position['X']) + len(player_position['O']) == 9:
        return True
    return False

#Function for a single Tic Tac Toe Game
def single_game(current_player):

    #Represents the Tic Tac Toe
    Values = [' ' for X in range(9)]

    #Stores the position occupied by X and O
    player_position = {'X':[], 'O':[]}

    #Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_t_t(Values)

        #Try exception block for MOVE input
        try:
            print("Player ", current_player, " turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Wrong input!!! Try again")
            continue

        #Sanity check for MOVE inpout
        if move <1 or move > 9:
            print("Please choose the right number between 1 to 9 ")
            continue

        #Check if the cell is occupied or not
        if Values[move-1] != '':
            print(" The place you have chosen is already filled. Try again!!")
            continue
        # Update game stutus
        Values[move-1] = current_player

        #Updating players positions
        player_position[current_player].append(move)

        #function call for checking winner
        if check_winner(player_position, current_player):
            print_tic_t_t(Values)
            print("Player ", current_player, "has won the game!!")
            print("\n")
            return current_player

        #Function for checking draw game
        if check_draw(player_position):
            print_tic_t_t(Values)
            print("Game is a Draw")
            print("\n")
            return 'D'

        #Switch player moves
        if current_player == 'X' :
            current_player == 'O'
        else:
            current_player ='X'

if __name__ == "__main__":
    print("Player 1 datails ")
    play1 = input("Enter the name of the Player : ")
    print("\n")

    print("Player 2 Details")
    play2 = input("Enter the name of Player 2 :")
    print("\n")
    #Store the player who chooses X and O
    current_player = play1

    #store the choice of player charecter
    player_choice = {'X', "", 'O' ""}

    #Store the options
    Option = ['X', 'O']

    #Stores the Scoreboard  details 
    score_board = {play1: 0, play2: 0}
    print_scoreboard(score_board)

    # Game Loop for a serios of Tic Tac Toe Game
    # The loop runs untill either of the player choose to quit
    while True:

        # Player choice menu
        print("Turn to choose for", current_player)
        print("Emter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 for Quit")

        #Try exception for CHOICE input
        try:
            choice = int(input())
        except ValueError:
            print("Wrong input!! Try again\n")
            continue

        # Condition for player choice
        if choice == 1:
            player_choice['X'] = current_player
            if current_player == play1:
                player_choice['0'] = play2
            else:
                player_choice['0'] = play1
        elif choice == 2:
            player_choice['0'] = current_player
            if current_player == play1:
                player_choice['X'] = play2
            else:
                player_choice['X'] = play1
        
        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break

        else:
            print("Wrong choice!!! Try again\n")
