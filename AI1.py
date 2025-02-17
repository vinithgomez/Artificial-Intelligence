def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    for _ in range(9):  # Maximum of 9 moves
        print_board(board)
        player = players[turn % 2]
        row, col = map(int, input(f"Player {player}, enter row and column (0-2): ").split())

        while board[row][col] != " ":
            print("Position already taken. Try again.")
            row, col = map(int, input(f"Player {player}, enter row and column (0-2): ").split())

        board[row][col] = player
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return

        turn += 1

    print_board(board)
    print("It's a draw!")

tic_tac_toe()
