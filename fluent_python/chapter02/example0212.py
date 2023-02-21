def print_board(board):
    for row in board:
        for item in row:
            print(item + ' ', end='')
        print('')
    print('')

board = [['_'] * 3 for i in range(3)]
print_board(board)
board[1][2] = 'X'
print_board(board)