from tkinter import *
import tkinter.messagebox as tk
from teams import main
from PIL import Image, ImageTk


def instructionsPopUp():
    w = """Welcome to my Valorant 5v5 Team Randomizer!
    
    With this program the hope is to create evenly matched
    
    teams, based on current competitive ranks while still 
    
    keeping it random enough for you and your friends to 
    
    continue to have fun playing custom valorant games. 
    
    To get your two teams of attackers and defenders simply 
    
    enter everyon's names into their own text box and their 
    
    respective ranks into the option menu beside the text 
    
    box you entered their name in. Thank you and have fun!"""

    tk.showinfo('Welcome to my Valorant Match Maker!', w)

def getPlayers():
    p1 = [player1.get(), oneOptionVar.get()]
    p2 = [player2.get(), twoOptionVar.get()]
    p3 = [player3.get(), threeOptionVar.get()]
    p4 = [player4.get(), fourOptionVar.get()]
    p5 = [player5.get(), fiveOptionVar.get()]
    p6 = [player6.get(), sixOptionVar.get()]
    p7 = [player7.get(), sevenOptionVar.get()]
    p8 = [player8.get(), eightOptionVar.get()]
    p9 = [player9.get(), nineOptionVar.get()]
    p10 = [player10.get(), tenOptionVar.get()]

    print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
    guiInput = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    print(guiInput)
    print('guiInput 00' ,guiInput[0][0])

    team1, team2 = main(guiInput)

    w = f'Attackers: {team1[0][:-1]}, {team1[1][:-1]}, {team1[2][:-1]}, {team1[3][:-1]}, {team1[4][:-1]}\n\nDefenders: {team2[0][:-1]}, {team2[1][:-1]}, {team2[2][:-1]}, {team2[3][:-1]}, {team2[4][:-1]}'

    tk.showinfo('Teams Created', w)

    """ p1 = player1.get()
    rank1 = oneOptionVar.get()
    p1 = [p1, rank1]
    print(p1)

    testP2 = [player2.get(), twoOptionVar.get()]
    print(testP2) """
 
#MAIN
root = Tk()
mainframe = Frame(root)


#WIDGETS

#title
#logoImg = Image.open('val.png').resize((371, 53))
#logoPhoto = ImageTk.PhotoImage(logoImg)
#titleLabel = Label(mainframe, image=logoPhoto)
titleLabel = Label(mainframe, text='Valorant', fg='red', font=('Bernard MT Condensed', 45))

""" headerCv = Canvas(mainframe, width=400, height=100)
headerCv.pack(expand=YES, fill=BOTH)
val = PhotoImage(file='val.png')
headerCv.create_image(200, 100, image=val, anchor=NW) """

"""valImage = Image.open(r'val.png').resize((400,100))
valPhoto = ImageTk.PhotoImage(valImage)

headerCv.create_image(200, 100, image=valPhoto) """

#ranks
ranks = ['iron1','iron2','iron3','bronze1','bronze2','bronze3','silver1','silver2','silver3','gold1','gold2','gold3','plat1','plat2','plat3','diamond1','diamond2','diamond3','immortal1','immortal2','immortal3','valorant']

#left
player1 = StringVar()
playerOneEntry = Entry(mainframe, width=20, text="", font=("Arial", 10), textvariable=player1)

oneOptionVar = StringVar()
oneOptionVar.set('iron1')
rankOneOption = OptionMenu(mainframe, oneOptionVar, *ranks)

player2 = StringVar()
playerTwoEntry = Entry(mainframe, width=20, text="", font=("Arial", 10), textvariable=player2)

twoOptionVar = StringVar()
twoOptionVar.set('iron1')
rankTwoOption = OptionMenu(mainframe, twoOptionVar, *ranks)

player3 = StringVar()
playerThreeEntry = Entry(mainframe, width=20, text="", font=("Arial", 10), textvariable=player3)

threeOptionVar = StringVar()
threeOptionVar.set('iron1')
rankThreeOption = OptionMenu(mainframe, threeOptionVar, *ranks)

player4 = StringVar()
playerFourEntry = Entry(mainframe, width=20, text="", font=("Arial", 10), textvariable=player4)

fourOptionVar = StringVar()
fourOptionVar.set('iron1')
rankFourOption = OptionMenu(mainframe, fourOptionVar, *ranks)

player5 = StringVar()
playerFiveEntry = Entry(mainframe, width=20, text="", font=("Arial", 10), textvariable=player5)

fiveOptionVar = StringVar()
fiveOptionVar.set('iron1')
rankFiveOption = OptionMenu(mainframe, fiveOptionVar, *ranks)


#right
player6 = StringVar()
playerSixEntry = Entry(mainframe, width=20, text="", font=("Arial", 10), textvariable=player6)

sixOptionVar = StringVar()
sixOptionVar.set('iron1')
rankSixOption = OptionMenu(mainframe, sixOptionVar, *ranks)

player7 = StringVar()
playerSevenEntry = Entry(mainframe, width=20, text="", font=("Arial", 10), textvariable=player7)

sevenOptionVar = StringVar()
sevenOptionVar.set('iron1')
rankSevenOption = OptionMenu(mainframe, sevenOptionVar, *ranks)

player8 = StringVar()
playerEightEntry = Entry(mainframe, width=20, text="", font=("Arial", 10), textvariable=player8)

eightOptionVar = StringVar()
eightOptionVar.set('iron1')
rankEightOption = OptionMenu(mainframe, eightOptionVar, *ranks)

player9 = StringVar()
playerNineEntry = Entry(mainframe, width=20, text="", font=("Arial", 10), textvariable=player9)

nineOptionVar = StringVar()
nineOptionVar.set('iron1')
rankNineOption = OptionMenu(mainframe, nineOptionVar, *ranks)

player10 = StringVar()
playerTenEntry = Entry(mainframe, width=20, text="", font=("Arial", 10), textvariable=player10)

tenOptionVar = StringVar()
tenOptionVar.set('iron1')
rankTenOption = OptionMenu(mainframe, tenOptionVar, *ranks)

#instructions and enter buttons
info = Button(mainframe, text='INFO', command=instructionsPopUp, fg='blue')
info.config(height=3, width=15)

enter = Button(mainframe, text='CREATE TEAMS', command=getPlayers, fg='red')
enter.config(height=3, width=15)



#GRID
root.minsize(width=540, height=540)
mainframe.grid(row=1, column=1, padx=20)

#title
titleLabel.grid(row=1, column=1, columnspan=5, pady=30, sticky=EW)
#headerCv.grid(row=1, column=1, columnspan=5, pady=30, sticky=EW)

#left
playerOneEntry.grid(row=2, column=1, padx=6, pady=20)
rankOneOption.grid(row=2, column=2, padx=6, pady=20)

playerTwoEntry.grid(row=3, column=1, padx=6, pady=20)
rankTwoOption.grid(row=3, column=2, pady=20)

playerThreeEntry.grid(row=4, column=1, padx=6, pady=20)
rankThreeOption.grid(row=4, column=2, pady=20)

playerFourEntry.grid(row=5, column=1, padx=6, pady=20)
rankFourOption.grid(row=5, column=2, padx=6, pady=20)

playerFiveEntry.grid(row=6, column=1, padx=6, pady=20)
rankFiveOption.grid(row=6, column=2, padx=6, pady=20)

#right
playerSixEntry.grid(row=2, column=3, padx=6, pady=20)
rankSixOption.grid(row=2, column=4, padx=6, pady=20)

playerSevenEntry.grid(row=3, column=3, padx=6, pady=20)
rankSevenOption.grid(row=3, column=4, padx=6, pady=20)

playerEightEntry.grid(row=4, column=3, padx=6, pady=20)
rankEightOption.grid(row=4, column=4, padx=6, pady=20)

playerNineEntry.grid(row=5, column=3, padx=6, pady=20)
rankNineOption.grid(row=5, column=4, padx=6, pady=20)

playerTenEntry.grid(row=6, column=3, padx=6, pady=20)
rankTenOption.grid(row=6, column=4, padx=6, pady=20)

#buttons
info.grid(row=2, column=5, rowspan=3, padx=15, pady=15)
enter.grid(row=5, column=5, rowspan=2, padx=15, pady=15)

root.mainloop()
