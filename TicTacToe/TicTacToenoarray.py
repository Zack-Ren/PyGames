import pygame

ttt_board = [["-","-","-"],["-","-","-"],["-","-","-"]]

def draw_board():
    for i in range(3):
        print(ttt_board[i])

def endgame():
    for y in ttt_board:
        if y[0] == y[1] == y[2] and y[0] != "-":
            return True

    if ttt_board[0][0] == ttt_board[1][1] == ttt_board[2][2] and ttt_board[0][0] != "-":
        return True

    if ttt_board[0][2] == ttt_board[1][1] == ttt_board[2][0] and ttt_board[1][1] != "-" :
        return True

    for x in range(3):
        if ttt_board[0][x] == ttt_board[1][x] == ttt_board[2][x] and ttt_board[0][x] != '-':
            return True
            
    else:
        return False


def tie_game():
    counter = 0

    for b in ttt_board:
        counter = b.count("-") + counter

    return counter == 0


def ttt_moves1():

    draw_board()
    row1 = int(input("Player 1: What row do you want to place your 'x': ")) - 1
    column1 = int(input("Player 1: What column do you want to 'x': ")) - 1

    if row1 not in range(3) or column1 not in range(3):

        print("Player 1: Please enter a valid row and column to place your x: ")

        return ttt_moves1()

    if ttt_board[row1][column1] == "x" or ttt_board[row1][column1] == "y":

        print("Player 1: That spot of the board is filled! Please Please enter a valid row and column to place your x: ")

        return ttt_moves1()

    if ttt_board[row1][column1] == "-":

        ttt_board[row1][column1] = "x"


        if endgame() == True:

            print("Game over. Player 1 wins!")
            return "Player 1"

        if endgame() == False and tie_game() == True:

            print("Game over. Tie game")
            return "Tie Game"

        return ttt_moves2()


def ttt_moves2():

    draw_board()
    row2 = int(input("Player 2: What row do you want to place your 'y': ")) - 1
    column2 = int(input("Player 2: What column do you want to 'y': ")) - 1

    if row2 not in range(3) or column2 not in range(3):
        print("Player 2: Please enter a valid row and column to place your y: ")

        return ttt_moves1()

    if ttt_board[row2][column2] == "x" or ttt_board[row2][column2] == "y":
        print("Player 2: That spot of the board is filled! Please Please enter a valid row and column to place your y: ")

        return ttt_moves1()

    if ttt_board[row2][column2] == "-":

        ttt_board[row2][column2] = "y"

        if endgame() == True:
            print("Game over. Player 2 wins!")
            return "Player 2"

        if endgame() == False and tie_game() == True:
            print("Game over. Tie game")
            return "Tie Game"

        return ttt_moves1()

play_game = ttt_moves1()




















