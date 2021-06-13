import tkinter
from tkinter import *
from tkinter import messagebox

top = Tk()
def hello():
   tkMessageBox.showinfo("Say Hello", "Hello World")

B1 = tkinter.Button(top, text = "Say Hello world", command = hello)
B1.pack()

top.mainloop()