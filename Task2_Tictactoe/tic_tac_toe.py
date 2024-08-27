from game_board import GameBoard
from ai_player import AIPlayer

def play_game():
    board = GameBoard()
    ai_player = AIPlayer('O')
    human_player = 'X'

    while True:
        board.print_board()

        if board.is_winner(ai_player.player):
            print("AI wins!")
            break
        if board.is_winner(human_player):
            print("You win!")
            break
        if board.is_full():
            print("It's a draw!")
            break

        if board.board.count(' ') % 2 == 1:
            # Human's turn
            move = int(input("Enter your move (0-8): "))
            if move not in board.available_moves():
                print("Invalid move. Try again.")
                continue
            board.make_move(move, human_player)
        else:
            # AI's turn
            move = ai_player.get_best_move(board)
            board.make_move(move, ai_player.player)
            print(f"AI chose position {move}")

if __name__ == "__main__":
    play_game()
