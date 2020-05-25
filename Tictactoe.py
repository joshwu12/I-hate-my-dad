
def display_board(board):

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def player_input():
    yee = True
    while yee == True:
        answer = input('Player 1: Choose X or O')
        if answer == 'X' or answer == 'x':

            return ("Player 1 is 'X', Player 2 is 'O'")

        elif answer == 'O' or answer == 'o' or answer == '0':

            return "Player 1 is 'O', Player 2 is 'X'"
        else:
            yee == False
    while not yee:
        yee == True

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    if board[7] == mark and board[5] == mark and board[3] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[7] == mark and board[4] == mark and board[1] == mark:
        return True
    elif board[8] == mark and board[5] == mark and board[2] == mark:
        return True
    elif board[9] == mark and board[6] == mark and board[3] == mark:
        return True
    else:
        return False

import random

def choose_first():
    if random.randint(1 ,2) == 1:
        return 'Player1 goes first'
    else:
        return 'Player2 goes first'


def space_check(board, position):
    if board[int(position)] == ' ':
        return 'Open'
    else:
        return 'Occupied'

def full_board_check(board):
    square_total = -1
    for num in board:
        if num != ' ':
            square_total += 1
        else:
            break
    if square_total == 9:
        return True
    else:
        return False


def player_choice(board):
    Yee = True
    while Yee == True:
        position = input('Position (1-9)')
        if int(position) >= 1 and int(position) <= 9:
            space_check_v = space_check(board, int(position))
            if space_check_v == 'Occupied':
                Yee == True
            else:
                return int(position)
        else:
            pass


def replay():
    Yee = True
    while Yee == True:
        playagain = input('Do you want to play again').upper()
        if playagain == 'YES':
            return True
        elif playagain == 'NO':
            return False
        else:
            pass
    else:
        pass


print('Welcome to Tic Tac Toe!')

while True:

    gameboard = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    who_is_what = player_input()
    if who_is_what == "Player 1 is 'X', Player 2 is 'O'":
        player1_marker = 'X'
        player2_marker = 'O'
    else:
        player1_marker = 'O'
        player2_marker = 'X'
    turn = choose_first()
    print(turn)
    choose_first()

    play_game = input("Ready to play?")

    if play_game == 'yes' or play_game == 'y':

        on = True
    else:
        on = False

    while on:
        if turn == 'Player1 goes first':

            display_board(gameboard)
            position_choice = player_choice(gameboard)
            place_marker(gameboard, player1_marker, position_choice)

            if win_check(gameboard, player1_marker) == True:
                display_board(gameboard)
                print("Player 1 won!")
                on = False
            else:
                if full_board_check(gameboard) == True:
                    display_board(gameboard)
                    print("Tie Game")
                    on = False
                else:
                    turn = 'Player2 goes first'


        else:

            display_board(gameboard)
            position_choice = player_choice(gameboard)
            place_marker(gameboard, player2_marker, position_choice)

            if win_check(gameboard, player2_marker) == True:
                display_board(gameboard)
                print("Player 2 won!")
                on = False
            else:
                if full_board_check(gameboard) == True:
                    display_board(gameboard)
                    print("Tie Game")
                    on = False
                else:
                    turn = 'Player1 goes first'

    if not replay():
        break