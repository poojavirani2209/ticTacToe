from player import User, Computer
from board import Board
from gameanalyser import GameAnalyser


class GameMaintainer:
    players = []
    playboard = Board()
    currentPlayerIndex = 0
    gameAnalyser = GameAnalyser()
    lastRow = 0
    lastCol = 0

    def getBoard(self):
        return self.playboard

    def addNewPlayer(self, name, icon):
        user = User(name, icon)
        self.players.append(user)

    def addComputerPlayer(self, icon):
        user = Computer(icon)
        self.players.append(user)

    def createBoard(self, size):
        self.playboard.createBoard(size)

    def addValueToBoard(self, row, column):
        self.playboard.addValueToBoard(row, column, self.getCurrentPlayerIcon())
        self.lastRow = row
        self.lastCol = column

    def changeCurrentPlayer(self):
        if self.currentPlayerIndex < len(self.players) - 1:
            self.currentPlayerIndex = self.currentPlayerIndex + 1
        else:
            self.currentPlayerIndex = 0

    def getCurrentPlayerName(self):
        return self.players[self.currentPlayerIndex].name

    def getPlayerByName(self, name):
        for i in self.players:
            if i.name == name:
                return i

    def getCurrentPlayerIcon(self):
        return self.players[self.currentPlayerIndex].icon

    def analyzeBoard(self):
        self.gameAnalyser.analyze(self.playboard.board)

    def getLastRow(self):
        return self.lastRow

    def getLastCol(self):
        return self.lastCol
