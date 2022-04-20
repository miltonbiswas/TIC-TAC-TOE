# This is Tac-Tac-Toe game.
#The author is Milton Biswas.

#Functions to be print on Tic Tac Toe Board
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