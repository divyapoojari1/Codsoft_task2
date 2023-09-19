import random
print('Instruction')
print('For specifing position')
print('top-L, top-M, top-R, mid-L, mid-M, mid-R,low-L, low-M, low-R ')

Board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}




def printBoard(board):
    print(board['top-L'] + ' |' + board['top-M'] + ' |' + board['top-R'])
    print('- + - + -')
    print(board['mid-L'] + ' |' + board['mid-M'] + ' |' + board['mid-R'])
    print('- + - + -')
    print(board['low-L'] + ' |' + board['low-M'] + ' |' + board['low-R'])


def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    return (
            (board['top-L'] == board['top-M'] == board['top-R'] == player) or
            (board['mid-L'] == board['mid-M'] == board['mid-R'] == player) or
            (board['low-L'] == board['low-M'] == board['low-R'] == player) or
            (board['top-L'] == board['mid-L'] == board['low-L'] == player) or
            (board['top-M'] == board['mid-M'] == board['low-M'] == player) or
            (board['top-R'] == board['mid-R'] == board['low-R'] == player) or
            (board['top-L'] == board['mid-M'] == board['low-R'] == player) or
            (board['top-R'] == board['mid-M'] == board['low-L'] == player)
    )


def is_board_full(board):
    return all(board[spot] != ' ' for spot in board)


def minimax(board, depth, maximizing_player):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for spot in board:
            if board[spot] == ' ':
                board[spot] = 'O'
                eval = minimax(board, depth + 1, False)
                board[spot] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for spot in board:
            if board[spot] == ' ':
                board[spot] = 'X'
                eval = minimax(board, depth + 1, True)
                board[spot] = ' '
                min_eval = min(min_eval, eval)
        return min_eval


def find_best_move(board):
    best_eval = float('-inf')
    best_move = None
    for spot in board:
        if board[spot] == ' ':
            board[spot] = 'O'
            eval = minimax(board, 0, False)
            board[spot] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = spot
    return best_move


turn = 'X'
while True:
    printBoard(Board)

    if turn == 'X':
        print('Turn for X. Move on which space?')
        move = input()
    else:
        print('AI (O) is thinking...')
        move = find_best_move(Board)

    if Board[move] == ' ':
        Board[move] = turn
    else:
        print('Invalid move. Try again.')
        continue

    if check_win(Board, turn):
        printBoard(Board)
        print(turn + ' wins!')
        break
    elif is_board_full(Board):
        printBoard(Board)
        print('It\'s a draw!')
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
