#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

first_flag = 1
c = 8
count_d_1 = 8
HUMAN = -1
COMP = +1
COMP2 = -1
board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


def evaluate(state):
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    elif wins(state, COMP2):
        score = -1
    else:
        score = 0
    return score


def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[0][1], state[0][2], state[0][3]],
        [state[0][2], state[0][3], state[0][4]],
        [state[1][0], state[1][1], state[1][2]],
        [state[1][1], state[1][2], state[1][3]],
        [state[1][2], state[1][3], state[1][4]],
        [state[2][0], state[2][1], state[2][2]],
        [state[2][1], state[2][2], state[2][3]],
        [state[2][2], state[2][3], state[2][4]],
        [state[3][0], state[3][1], state[3][2]],
        [state[3][1], state[3][2], state[3][3]],
        [state[3][2], state[3][3], state[3][4]],
        [state[4][0], state[4][1], state[4][2]],
        [state[4][1], state[4][2], state[4][3]],
        [state[4][2], state[4][3], state[4][4]],
        [state[0][0], state[1][0], state[2][0]],
        [state[1][0], state[2][0], state[3][0]],
        [state[1][0], state[2][0], state[3][0]],
        [state[2][0], state[3][0], state[4][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[1][1], state[2][1], state[3][1]],
        [state[2][1], state[3][1], state[4][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[1][2], state[2][2], state[3][2]],
        [state[2][2], state[3][2], state[4][2]],
        [state[0][3], state[1][3], state[2][3]],
        [state[1][3], state[2][3], state[3][3]],
        [state[2][3], state[3][3], state[4][3]],
        [state[0][4], state[1][4], state[2][4]],
        [state[1][4], state[2][4], state[3][4]],
        [state[2][4], state[3][4], state[4][4]],
        [state[0][0], state[1][1], state[2][2]],
        [state[1][1], state[2][2], state[3][3]],
        [state[2][2], state[3][3], state[4][4]],
        [state[1][0], state[2][1], state[3][2]],
        [state[2][1], state[3][2], state[4][3]],
        [state[2][0], state[3][1], state[4][2]],
        [state[0][1], state[1][2], state[2][3]],
        [state[1][2], state[2][3], state[3][4]],
        [state[0][2], state[1][3], state[2][4]],
        [state[0][4], state[1][3], state[2][2]],
        [state[1][3], state[2][2], state[3][1]],
        [state[2][2], state[3][1], state[4][0]],
        [state[3][0], state[1][2], state[2][1]],
        [state[1][2], state[2][1], state[3][0]],
        [state[2][0], state[1][1], state[0][2]],
        [state[1][4], state[2][3], state[3][2]],
        [state[2][3], state[3][2], state[1][4]],
        [state[2][4], state[3][3], state[4][2]],
    ]

    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP) or wins(state, COMP2)


def empty_cells(state):
    cells = []
    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    return cells


def valid_move(x, y):
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def abminimax(state, depth, alpha, beta, player):
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        global count_d_1, f
        count_d_1 = c
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = abminimax(state, depth - 1, alpha, beta, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > alpha:
                alpha = score[2]
                best = score
        else:
            if score[2] < beta:
                beta = score[2]
                best = score

        if alpha >= beta:
            break

    return best


def clean():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(state, c_choice, h_choice):
    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '-------------------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    global count_d_1
    depth = count_d_1
    count_d_1 = count_d_1 - 1
    if depth == 0 or game_over(board):
        return

    clean()
    render(board, c_choice, h_choice)

    if depth == c and first_flag:
        x = choice([0, 1, 2, 3, 4])
        y = choice([0, 1, 2, 3, 4])

    else:
        move = abminimax(board, depth, -infinity, infinity, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)


def ai_turn2(c_choice, h_choice):
    global count_d_1
    depth = count_d_1
    count_d_1 = count_d_1 - 1
    if depth == 0 or game_over(board):
        return

    clean()
    render(board, c_choice, h_choice)

    if depth == c and first_flag:
        x = choice([0, 1, 2, 3, 4])
        y = choice([0, 1, 2, 3, 4])

    else:
        move = abminimax(board, depth,-infinity,infinity, COMP2)
        x, y = move[0], move[1]

    set_move(x, y, COMP2)
    time.sleep(1)


def human_turn(c_choice, h_choice):
    global count_d_1
    depth = count_d_1
    count_d_1 = count_d_1 - 1
    if depth == 0 or game_over(board):
        return

    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [0, 3], 5: [0, 4],
        6: [1, 0], 7: [1, 1], 8: [1, 2], 9: [1, 3], 10: [1, 4],
        11: [2, 0], 12: [2, 1], 13: [2, 2], 14: [2, 3], 15: [2, 4],
        16: [3, 0], 17: [3, 1], 18: [3, 2], 19: [3, 3], 20: [3, 4],
        21: [4, 0], 22: [4, 1], 23: [4, 2], 24: [4, 3], 25: [4, 4],

    }

    clean()
    render(board, c_choice, h_choice)

    while move < 1 or move > 25:
        try:
            move = int(input('Use numpad (1..25): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main():
    clean()
    h_choice = ''
    c_choice = ''
    first = ''

    print("Enter 1 or 2")
    print("1.computer with human")
    print('2.computer with computer')
    mode = input()
    if mode == '1':
        while h_choice != 'R' and h_choice != 'G':
            try:
                print('')
                h_choice = input('Choose G or R\nChosen: ').upper()
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')

        if h_choice == 'G':
            c_choice = 'R'
        else:
            c_choice = 'G'

        clean()
        while first != 'Y' and first != 'N':
            try:
                first = input('First to start?[y/n]: ').upper()
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')

        # Main loop of this game
        if first == 'N':
            while len(empty_cells(board)) > 0 and not game_over(board):
                global c
                c = 8
                ai_turn(c_choice, h_choice)
                human_turn(c_choice, h_choice)

        else:
            while len(empty_cells(board)) > 0 and not game_over(board):
                c = 7
                human_turn(c_choice, h_choice)
                ai_turn(c_choice, h_choice)

        if wins(board, HUMAN):
            clean()
            print(f'Human turn [{h_choice}]')
            render(board, c_choice, h_choice)
            print('YOU WIN!')
        elif wins(board, COMP):
            clean()
            print(f'Computer turn [{c_choice}]')
            render(board, c_choice, h_choice)
            print('YOU LOSE!')
        else:
            clean()
            render(board, c_choice, h_choice)
            print('DRAW!')

    if mode == '2':
        while c_choice != 'R' and c_choice != 'G':
            try:
                print('')
                c_choice = input('Choose G or R\nChosen: ').upper()
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')


        if c_choice == 'G':
            h_choice = 'R'
        else:
            h_choice = 'G'

        clean()

        while len(empty_cells(board)) > 0 and not game_over(board):
            c = 8
            ai_turn(c_choice, h_choice)
            ai_turn2(c_choice, h_choice)
            global first_flag
            first_flag = 0

        if wins(board, COMP):
            clean()
            render(board, c_choice, h_choice)
            print('computer1 win!')
        elif wins(board, COMP2):
            clean()
            render(board, c_choice, h_choice)
            print('computer2 win!')
        else:
            clean()
            render(board, c_choice, h_choice)
            print('DRAW!')

    exit()


if __name__ == '__main__':
    main()