class GameBoard:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        print(f"""
         {self.board[0]} | {self.board[1]} | {self.board[2]}
        ---|---|---
         {self.board[3]} | {self.board[4]} | {self.board[5]}
        ---|---|---
         {self.board[6]} | {self.board[7]} | {self.board[8]}
        """)

    def is_full(self):
        return ' ' not in self.board

    def is_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
