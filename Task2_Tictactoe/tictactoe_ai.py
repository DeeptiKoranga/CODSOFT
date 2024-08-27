import random

# Define the Tic-Tac-Toe board
board = [" " for _ in range(9)]

def print_board():
    """Print the current state of the board."""
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def is_winner(board, player):
    """Check if the given player has won."""
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def is_draw(board):
    """Check if the game is a draw."""
    return " " not in board

def minimax(board, depth, is_maximizing):
    """Minimax algorithm with recursion to make AI unbeatable."""
    if is_winner(board, "O"):
        return 1
    if is_winner(board, "X"):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    """Make the best possible move for AI using Minimax."""
    best_score = -float("inf")
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def player_move():
    """Ask the player for their move."""
    while True:
        move = input("Enter your move (1-9): ")
        try:
            move = int(move) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

# Main game loop
while True:
    print_board()
    if is_winner(board, "O"):
        print("AI wins!")
        break
    if is_winner(board, "X"):
        print("You win!")
        break
    if is_draw(board):
        print("It's a draw!")
        break

    player_move()
    if not is_draw(board) and not is_winner(board, "X"):
        ai_move()

    print_board()
    if is_winner(board, "O"):
        print("AI wins!")
        break
    if is_winner(board, "X"):
        print("You win!")
        break
    if is_draw(board):
        print("It's a draw!")
        break
