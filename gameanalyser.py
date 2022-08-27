class GameAnalyser:
    def analyze(self, board):
        return self.check_for_horizontal(board) or self.check_for_vertical(board) or self.check_for_diagonals(board)

    def check_for_tie(self, board):
        for i in range(0, len(board)-1):
            for j in range(0,len(board)-1):
                if '' in board[i][j]:
                    return bool(0)

    def check_for_horizontal(self, board):
        for i in range(len(board)):
            return len(set(board[i])) == 1 and '' not in set(board[i])

    def check_for_vertical(self, board):
        return self.check_for_horizontal(list(zip(*reversed(board))))

    def check_for_diagonals(self, board):
        return (len(set([r[i] for i, r in enumerate(board)])) == 1 and '' not in set(
            [r[i] for i, r in enumerate(board)])) or (
                       len(set([r[i] for i, r in enumerate(board[::-1])])) == 1 and '' not in set(
                   [r[i] for i, r in enumerate(board[::-1])]))

