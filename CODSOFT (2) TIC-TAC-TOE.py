import math

def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    if check_win(board, "O"):
        return 1
    if check_win(board, "X"):
        return -1
    if board_full(board):
        return 0

    if is_maximizing:  # AI's turn (O)
        best = -math.inf
        for i, j in get_available_moves(board):
            board[i][j] = "O"
            val = minimax(board, depth + 1, False)
            board[i][j] = " "
            best = max(best, val)
        return best
    else:  # Human's turn (X)
        best = math.inf
        for i, j in get_available_moves(board):
            board[i][j] = "X"
            val = minimax(board, depth + 1, True)
            board[i][j] = " "
            best = min(best, val)
        return best

def ai_move(board):
    best_score = -math.inf
    move = None
    for i, j in get_available_moves(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            move = (i, j)
    if move:  # place AI move
        board[move[0]][move[1]] = "O"

def main():
    board = [[" "]*3 for _ in range(3)]
    print("Welcome to Tic Tac Toe! You are X, AI is O.")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                move = input("Enter your move (row col): ")
                row, col = map(int, move.strip().split())
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell already taken. Try again.")
            except:
                print("Invalid input. Please enter row and column as: row col (e.g. 0 1)")
        
        print_board(board)

        if check_win(board, "X"):
            print("🎉 You win!")
            break
        if board_full(board):
            print("🤝 It's a draw!")
            break

        # AI move
        ai_move(board)
        print("AI's move:")
        print_board(board)

        if check_win(board, "O"):
            print("💻 AI wins!")
            break
        if board_full(board):
            print("🤝 It's a draw!")
            break

if __name__ == "__main__":
    main()


