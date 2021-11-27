import tkinter
from tkinter.ttk import *

from time import strftime

root = tkinter.Tk()
root.title("Clock")

def time():
    string = strftime("%H :%M :%S ")
    label.config(text = string)
    label.after(1000,time)

label = Label(root, font=("calibri", 80), background = "black" , foreground = "blue")
label.pack(anchor = "center")
time()

tkinter.mainloop()
