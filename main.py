from interfaces.UI import startApplication as UIstart
from interfaces.console import start_application as consoleStart


def game_interface(argument):
    match argument:
        case 1:
            UIstart()
        case 2:
            consoleStart()
    continue_playing = input("Do you want to continue playing")
    if continue_playing == "yes":
        start_playing()

def start_playing():
    text = int(input("UI(1) or Console(2) game?"))
    game_interface(text)

if __name__ == '__main__':
    start_playing()

