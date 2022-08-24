from board import Board


class Player:
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon


class Computer(Player):
    def __init__(self, icon, name="computer"):
        Player.__init__(self, name, icon)

    def play(self,board,boardSize, icon):
        for i in range(boardSize - 1):
            for j in range(boardSize - 1):
                if board.checkIfCellIsEmpty(i,j):
                    board.addValueToBoard(i, j, icon)
                    return i, j


class User(Player):
    def __init__(self, name, icon):
        Player.__init__(self, name, icon)
