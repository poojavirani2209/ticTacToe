class GameAnalyser:
    def analyze(self, board):
        return self.checkForHorizontal(board) or self.checkForVertical(board) or self.checkForDiagonals(board)

    def checkForHorizontal(self, board):
        for i in range(len(board)):
            return len(set(board[i])) == 1 and '' not in set(board[i])

    def checkForVertical(self, board):
        return self.checkForHorizontal(list(zip(*reversed(board))))

    def checkForDiagonals(self, board):
        return (len(set([r[i] for i, r in enumerate(board)])) == 1 and '' not in set(
            [r[i] for i, r in enumerate(board)])) or (
                           len(set([r[i] for i, r in enumerate(board[::-1])])) == 1 and '' not in set(
                       [r[i] for i, r in enumerate(board[::-1])]))
