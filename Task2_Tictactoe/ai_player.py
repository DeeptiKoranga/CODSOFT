class AIPlayer:
    def __init__(self, player):
        self.player = player
        self.opponent = 'O' if player == 'X' else 'X'

    def minimax(self, board, depth, is_maximizing, alpha, beta):
        if board.is_winner(self.player):
            return 10 - depth
        if board.is_winner(self.opponent):
            return depth - 10
        if board.is_full():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for move in board.available_moves():
                board.make_move(move, self.player)
                score = self.minimax(board, depth + 1, False, alpha, beta)
                board.board[move] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = float('inf')
            for move in board.available_moves():
                board.make_move(move, self.opponent)
                score = self.minimax(board, depth + 1, True, alpha, beta)
                board.board[move] = ' '
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return best_score

    def get_best_move(self, board):
        best_move = -1
        best_score = -float('inf')
        for move in board.available_moves():
            board.make_move(move, self.player)
            score = self.minimax(board, 0, False, -float('inf'), float('inf'))
            board.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_move
