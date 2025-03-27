from tkinter import *
from random import randint

root = Tk()
dice = 6

def dice_type(dicesides) : 
    print(dicesides)
    global dice
    dice = dicesides
    

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Dice", menu=filemenu)
filemenu.add_command(label="D6", command=lambda: dice_type(6))
filemenu.add_command(label="D10", command=lambda: dice_type(10))
filemenu.add_command(label="D20", command=lambda: dice_type(20))


root.title("Dice game")
textbox = Label(root, text="")
textbox.pack()

def roll():
    roll = randint(1, dice)
    textbox.config(text=roll)

rollbutton = Button(root, text="Roll dice", width=50, command=roll)
rollbutton.pack()
button = Button(root, text="Quit", width=50, command=root.destroy)
button.pack()

root.mainloop()