from tkinter import *

root = Tk()
root.geometry(("200x200"))

score = 0
clickvalue = 1
clickupgradecost = 5

def click() :
    global score
    score += clickvalue

def clickupgrade() :
    global score
    global clickvalue
    global clickupgradecost
    if score >= clickupgradecost :
        score -= clickupgradecost
        clickvalue += 1
        clickupgradecost = round(clickupgradecost*1.2)
    else :
        print("can't afford")

def updateui() : 
    scorebox.config(text=score)
    clicker.config(text=f"click!(+{clickvalue})")
    clickupgrade.config(text=f"+1 score per click cost: {clickupgradecost}")

    root.after(50,updateui)

root.title("Clicker Game")

scorebox = Label(root, text=score)
scorebox.pack()

clicker = Button(root, text=f"click!(+{clickvalue})", width=25, command=click)
clicker.pack()

clickupgrade = Button(root, text=f"+1 score per click cost: {clickupgradecost}", width=50, command=clickupgrade)
clickupgrade.pack()

updateui()

root.mainloop()

