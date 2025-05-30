import tkinter as tk
import tkinter.font as font


global gui, root

nextIcon = True

def GUI():
    gui = tk.Tk()
    gui.geometry("620x620")
    gui.resizable(False, False)
    gui.title("Tic-Tac-Toe")
    global btnFont, etFont
    btnFont = font.Font(size=200)
    etFont = font.Font(size=65)

    return gui

########################################################

def backPanel(gui):
    root = tk.Canvas(master=gui, bg="#AAAAAA", relief="flat")
    root.place(relwidth=1, relheight=1)

    return root

########################################################

def endPanel(gui, won):
    panel = tk.Frame(master=gui, bg="#ABCABC", relief="flat")
    panel.place(relwidth=1, relheight=1)
    if won == 0:
        ms = "Circle Won!"
        pass
    elif won == 1:
        ms = "Cross Won!"
        pass
    else:
        ms = "Tie!"
        pass
    print(ms)
    print("-"*20)
    text = tk.Label(master=panel, font=etFont, text=f"{ms}")
    text.place(rely=.4, relx=.5, anchor="center")

    def end(exit):
        if exit:
            tk._exit(-2)
            pass
        global gui, tiles
        gui.destroy()
        main()
        pass


    ExitBtn = tk.Button(master=panel, text="Exit", font=etFont, command= lambda : end(True))
    ExitBtn.place(rely=.7, relx=.75, anchor="center")

    restartBtn = tk.Button(master=panel, text="Restart", font=etFont, command=lambda: end(False))
    restartBtn.place(rely=.7, relx=.35, anchor="center")

    pass
########################################################

def panelSetup(root):
    panels = [[None, None, None], [None, None, None], [None, None, None]]

    for y in range(3):
        for x in range(3):
            panel = tk.Canvas(master=root, bg="#FFFFFF", relief="raised", bd=5)
            panel.place(x=(x * 200) + 5, y=(y * 200) + 5)
            panels[y][x] = panel

    return panels

########################################################

def tileClick(buttons, x, y):
    tile(buttons, x, y)

########################################################

def setupBtns(panels):
    buttons = [[None, None, None], [None, None, None], [None, None, None]]

    for y in range(3):
        for x in range(3):
            def Clicked(X = x, Y = y):
                tileClick(buttons, X, Y)
                pass
            btn = tk.Button(master=panels[y][x], command=Clicked, text=f"-", font=btnFont)
            btn.place(width=200, height=200, x=7.5, y=7.5)
            buttons[y][x] = btn
            pass
        pass
    return buttons

########################################################
########################################################

def tileSet(buttons, y, x):
    button = buttons[y][x]

    if button["text"] == "-":
        global nextIcon
        if nextIcon:
            button["text"] = "X"
            tiles[y][x] = "X"
            nextIcon = False
        else:
            button["text"] = "O"
            tiles[y][x] = "O"
            nextIcon = True
        pass
    pass

########################################################

def checkTiles():
    winner = -1
    states = ["O", "X"]
    foundNone = False
    for state in states:
        ###########################################################################
        if tiles[0][2] == state and tiles[1][1] == state and tiles[2][0] == state:
            winner = states.index(state)
            pass
        ###########################################################################
        elif tiles[0][0] == state and tiles[1][1] == state and tiles[2][2] == state:
            winner = states.index(state)
            pass
        ###########################################################################
        else:
            for i in range(3):
                if tiles[i][0] == state and tiles[i][1] == state and tiles[i][2] == state:
                    winner = states.index(state)
                    pass
                if tiles[0][i] == state and tiles[1][i] == state and tiles[2][i] == state:
                    winner = states.index(state)
                    pass
                if not foundNone:
                    for x in range(3):
                        if tiles[x][i] is None:
                            foundNone = True
                            pass
                        pass
                    pass
                pass
            pass
        pass
    if not foundNone:
        winner = 2
    return winner

########################################################

def printTiles():
    print("-"*10)
    for i in range(3):
        print(tiles[i])
        pass
    pass

#########################################################
#########################################################

def main():
    global tiles, state
    tiles = [[None, None, None], [None, None, None], [None, None, None]]

    global gui, root
    gui = GUI()
    root = backPanel(gui)
    panels = panelSetup(root)
    buttons = setupBtns(panels)

    tk.mainloop()
    pass

def tile(buttons, x, y):
    tileSet(buttons, y, x)
    printTiles()
    won = checkTiles()
    if won != -1:
        root.destroy()
        endPanel(gui, won)
        pass

    pass


if __name__ == '__main__':
    main()
    pass
pass