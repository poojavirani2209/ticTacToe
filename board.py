class Board:
    board = []

    def getBoard(self):
        return self.board

    def getBoardSize(self):
        return len(self.board)

    def createBoard(self, size):
        self.board = [[''] * size for _ in range(size)]
        print(self.board)

    def addValueToBoard(self, row, column, icon):
        self.board[row][column] = icon
        print(self.board)

    def checkIfCellIsEmpty(self, row, column):
        return self.board[row][column] == ''
