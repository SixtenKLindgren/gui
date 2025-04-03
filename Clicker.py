from tkinter import *

root = Tk()
root.geometry(("200x200"))

score = 0
clickvalue = 1
clickupgradecost = 5
persecondupgradecost = 5
scorepersecond = 0

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

def persecondupgrade() :
    global score
    global persecondupgradecost
    global scorepersecond
    if score >= persecondupgradecost :
        score -= persecondupgradecost
        scorepersecond += 1
        persecondupgradecost = round(persecondupgradecost*1.2)
    else :
        print("can't afford")

def updateui() : 
    scorebox.config(text=score)
    clicker.config(text=f"click!(+{clickvalue}, +{scorepersecond}/s)")
    clickupgradebutton.config(text=f"+1 score per click cost: {clickupgradecost}")
    persecondupgradebutton.config(text=f"+1 score per second cost: {persecondupgradecost}")

    root.after(50,updateui)

def updatesecond() :
    global score
    score += scorepersecond

    root.after(1000,updatesecond)

root.title("Clicker Game")

scorebox = Label(root, text=score)
scorebox.pack()

clicker = Button(root, text=f"click!(+{clickvalue}, +{scorepersecond}/s)", width=25, command=click)
clicker.pack()

clickupgradebutton = Button(root, text=f"+1 score per click cost: {clickupgradecost}", width=50, command=clickupgrade)
clickupgradebutton.pack()

persecondupgradebutton = Button(root, text=f"+1 score per second cost: {persecondupgradecost}", width=50, command=persecondupgrade)
persecondupgradebutton.pack()

updatesecond()
updateui()

root.mainloop()

