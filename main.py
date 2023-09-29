from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("clock")
name = Label(root,font = ("ds-digital",100),background = "BLACK",foreground = "CYAN")
def time():
    format = strftime("%D %H %M %S %p")
    name.config(text = format)
    name.after(1000,time)

name.pack(anchor = "center")
time()
mainloop()
