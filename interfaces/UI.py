from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ticTacToe.gamemaintainer import GameMaintainer

maintainer = GameMaintainer()
btns = {}
window = Tk()

def addNewParticipant():
    txt = Entry(window, width=10)

    combo = Combobox(window)
    combo['values'] = ('X', '0')
    combo.current(0)

    addButton = Button(window, text="Add", command=lambda: maintainer.addNewPlayer(txt.get(), combo.get()))

    txt.pack()
    combo.pack()
    addButton.pack()


def defineBoard():
    txt = Entry(window, width=10)

    addButton = Button(window, text="Add", command=lambda: maintainer.createBoard(int(txt.get())))
    play = Button(window, text="Play", command=lambda: createPlayBoard(txt))

    maintainer.addComputerPlayer('0')  # todo need to change according to icon

    play.place(x=25, y=250)

    txt.pack()
    addButton.pack()


def createPlayBoard(txt):
    size = int(txt.get())
    btns_frame = Frame(window)
    btns_frame.pack()
    btn_num = -1

    for row in range(size):
        for col in range(size):
            btn_num = btn_num + 1

            b = Button(btns_frame ,command=lambda row=row, col=col, x=btn_num: [maintainer.addValueToBoard(row, col),
                                                                                changeText(row, col),
                                                                                nextPlayerMessage()])
            def changeText(row, col):
                btns[(row, col)]['text'] = maintainer.getCurrentPlayerIcon()

            b.grid(row=row, column=col)
            btns[(row, col)] = b


def nextPlayerMessage():
    current_player = maintainer.changeCurrentPlayer()
    if maintainer.checkForTie():
        messagebox.showinfo('Result!', "tiee")
    if maintainer.analyzeBoard():
        lbl = Label(window, text='Result!'+ maintainer.getCurrentPlayerName() + 'won', font=("Arial Bold", 10))
        lbl.pack()
        messagebox.showinfo('Result!', maintainer.getCurrentPlayerName() + "won")
    if current_player.is_computer_player():
        (i, j) = current_player.play(maintainer.getBoard(),maintainer.getCurrentPlayerIcon())
        btns[(i, j)]['text'] = maintainer.getCurrentPlayerIcon()
        nextPlayerMessage()


def refresh():
    window.destroy()
    startApplication()


def startApplication():
    window.title('TIC TAC TOE')

    addUserButton = Button(window, text="Add new participant", command=addNewParticipant)

    boardSize = Button(window, text="Define board size", command=defineBoard)

    addUserButton.pack()
    boardSize.pack()
    window.geometry('400x400')
    window.mainloop()
