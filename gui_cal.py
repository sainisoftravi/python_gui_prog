import tkinter
from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
            scvalue.set(value)
            screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = tkinter.Tk()
root.title("Simple Gui Calculator by Ravi Saini")
root.geometry("230x400")
root.resizable(0, 0)
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="Times 40 bold italic")
screen.pack(fill=X,ipadx=8,pady=10,padx=11)
f = Frame(root,bg="grey")
b = Button(f,text="7",font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)

b = Button(f,text="8",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)

b = Button(f,text="9",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)

b = Button(f,text="/",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="4",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)

b = Button(f,text="5",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)

b = Button(f,text="6",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)

b = Button(f,text="*",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="1",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)

b = Button(f,text="2",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)

b = Button(f,text="3",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)

b = Button(f,text="-",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="0",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)

b = Button(f,text="+",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)

b = Button(f,text="=",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)

b = Button(f,text="c",padx=10,pady=10,font="Helvetica 35 bold")
b.pack(side=LEFT,fill=BOTH,expand=TRUE)
b.bind("<Button-1>", click)
f.pack()


root.mainloop()
