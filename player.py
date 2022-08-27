import uuid
import random


class Player:
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon


class Computer(Player):
    def __init__(self, icon, name=str(uuid.uuid4())):
        Player.__init__(self, name, icon)

    def is_computer_player(self):
        return bool("true")

    def play(self, board, icon):
        i, j = self.get_random_position(board);
        board.addValueToBoard(i, j, icon)
        return i, j

    def get_random_position(self, board):
        while 1:
            row = random.randint(0, board.getBoardSize() - 1)
            col = random.randint(0, board.getBoardSize() - 1)
            if board.checkIfCellIsEmpty(row, col):
                return row, col


class User(Player):
    def __init__(self, name, icon):
        Player.__init__(self, name, icon)

    def play(self, row, col, board, icon):
        board.addValueToBoard(row, col, icon)

    def is_computer_player(self):
        return bool(0)
