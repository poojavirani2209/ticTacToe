from player import User, Computer
from board import Board
from gameanalyser import GameAnalyser


class GameMaintainer:
    players = []
    play_board = Board()
    current_player_index = 0
    game_analyzer = GameAnalyser()

    def getBoard(self):
        return self.play_board

    def addNewPlayer(self, name, icon):
        user = User(name, icon)
        self.players.append(user)

    def addComputerPlayer(self, icon):
        user = Computer(icon)
        self.players.append(user)

    def createBoard(self, size):
        self.play_board.createBoard(size)

    def addValueToBoard(self, row, column):
        self.play_board.addValueToBoard(row, column, self.getCurrentPlayerIcon())
        print(self.play_board)

    def changeCurrentPlayer(self):
        if self.current_player_index < len(self.players) - 1:
            self.current_player_index = self.current_player_index + 1
        else:
            self.current_player_index = 0
        return self.players[self.current_player_index]

    def getCurrentPlayerName(self):
        return self.players[self.current_player_index].name

    def getPlayerByName(self, name):
        for i in self.players:
            if i.name == name:
                return i

    def getCurrentPlayerIcon(self):
        return self.players[self.current_player_index].icon

    def analyzeBoard(self):
        return self.game_analyzer.analyze(self.play_board.board)

    def checkForTie(self):
        return self.game_analyzer.check_for_tie(self.play_board.board)

