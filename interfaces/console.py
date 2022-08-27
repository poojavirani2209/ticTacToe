from ticTacToe.gamemaintainer import GameMaintainer

maintainer = GameMaintainer()


def add_new_participant():
    name = input("Player name?")
    icon = input("icon?")

    maintainer.addNewPlayer(name, icon)


def add_participants(number_of_players):
    for i in range(number_of_players):
        add_new_participant()


def create_playBoard(board_size):
    size = int(board_size)
    maintainer.createBoard(size)


def play():
    while not maintainer.analyzeBoard():
        if maintainer.checkForTie():
            print("there is a tie!")
            break
        current_player = maintainer.changeCurrentPlayer()
        print(maintainer.getCurrentPlayerName() + " playing")
        if current_player.is_computer_player():
            current_player.play(maintainer.getBoard(), maintainer.getCurrentPlayerIcon())
        else:
            i, j = get_user_input()
            current_player.play(i, j, maintainer.getBoard(), maintainer.getCurrentPlayerIcon())
    print(maintainer.getCurrentPlayerName() + " won")


def get_user_input():
    row, col = input("Enter row and column").split()
    return int(row), int(col)


def refresh():
    start_application()


def start_application():
    board_size = int(input("Board Size?"))
    create_playBoard(board_size)

    computer_player = bool(input("Do you want computerPlayer?"))
    computer_player and maintainer.addComputerPlayer("C")

    number_of_players = int(input("how many user players?"))
    add_participants(number_of_players)

    play()
