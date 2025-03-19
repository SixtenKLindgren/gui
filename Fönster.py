from tkinter import *
from random import randint

for i in range(100) :
    width = randint(1,400)
    root = Tk()
    root.geometry(f"{i*10}x{width}")

root.mainloop()