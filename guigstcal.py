import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = ""


def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)
def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)
def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)
def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)
def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)
def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)
def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)
def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)
def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)
def btn_10_isclicked():
    global val
    val = val + "0"
    data.set(val)
def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)
def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)
def btn_plus_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)
def btn_minus_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)
def btn_multi_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)
def btn_divide_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_clear_isclicked():
    global A
    global operator
    global val
    A = 0
    operator = ""
    val = ""
    data.set(val)
def btn_result_isclicked():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        data.set(C)
        val= str(C)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        data.set(C)
        val= str(C)
    elif operator == "*":
        x = int((val2.split("*")[1]))
        C = A * x
        data.set(C)
        val= str(C)
    elif operator == "/":
        x = float((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error message","Division by zero is undefined")
            A = ""
            val = ""
            data.set(val)
        else:
            C = float(A / x)
            data.set(C)
            val = str(C)

        data.set(C)
        val= str(C)

root = tkinter.Tk()
root.title("Simple Gui Calculator by Ravi")
root.geometry("250x400+300+300")
root.resizable(0, 0)
data = StringVar()
lb1 = Label(root, text="Label", anchor=SE,textvariable=data,font="Times 30 bold italic", bg="grey", fg="black")
lb1.pack(expand=TRUE, fill=BOTH,)

btnrow1 = Frame(root, bg="grey")
btnrow1.pack(expand=TRUE, fill=BOTH, )

btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH, )

btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH, )

btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH, )
btnrow5 = Frame(root)
btnrow5.pack(expand=TRUE, fill=BOTH, )
# Button Calling
btn1 = Button(btnrow1, text="1", font=("Verdana Bold italic", 22), relief=RAISED, border=0, command=btn_1_isclicked, )
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow1, text="2", font=("Verdana Bold italic", 22), relief=RAISED, border=0, command=btn_2_isclicked,)
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow1, text="3", font=("Verdana Bold italic", 22), relief=RAISED, border=0,command=btn_3_isclicked,)
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4 = Button(btnrow1, text="+", font=("Verdana Bold italic", 22), relief=RAISED, border=0, fg="green",command=btn_plus_isclicked,)
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)


# Second Row


btn1 = Button(btnrow2, text="4", font=("Verdana Bold italic", 22), relief=RAISED, border=0,command=btn_4_isclicked,)
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow2, text="5", font=("Verdana Bold italic", 22), relief=RAISED, border=0,command=btn_5_isclicked,)
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow2, text="6", font=("Verdana Bold italic", 22), relief=RAISED, border=0,command=btn_6_isclicked,)
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4 = Button(btnrow2, text="-", font=("Verdana Bold italic", 22), relief=RAISED, border=0, fg="green",command=btn_minus_isclicked)
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Third Row


btn1 = Button(btnrow3, text="7", font=("Verdana Bold italic", 22), relief=RAISED, border=0,command=btn_7_isclicked,)
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow3, text="8", font=("Verdana Bold italic", 22), relief=RAISED, border=0,command=btn_8_isclicked,)
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow3, text="9", font=("Verdana Bold italic", 22), relief=RAISED, border=0,command=btn_9_isclicked,)
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4 = Button(btnrow3, text="*", font=("Verdana Bold italic", 22), relief=RAISED, border=0, fg="green",command=btn_multi_isclicked)
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Forth Row


btn1 = Button(btnrow4, text="c", font=("Verdana Bold italic", 22), relief=RAISED, border=0, fg="red",command=btn_clear_isclicked)
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow4, text="0", font=("Verdana Bold italic", 22), relief=RAISED, border=0,command=btn_10_isclicked,)
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow4, text="=", font=("Verdana Bold italic", 22), relief=RAISED, border=0, fg="purple",command=btn_result_isclicked)
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4 = Button(btnrow4, text="/", font=("Verdana Bold italic", 22), relief=RAISED, border=0, fg="green",command=btn_divide_isclicked)
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

## Gst Calculator

btn1 = Button(btnrow5, text="5%", font=("Verdana Bold italic", 22), relief=RAISED, border=0, fg="red",command=btn_clear_isclicked)
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow5, text="10%", font=("Verdana Bold italic", 22), relief=RAISED, border=0,command=btn_10_isclicked,)
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow5, text="18%", font=("Verdana Bold italic", 22), relief=RAISED, border=0, fg="purple",command=btn_result_isclicked)
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4 = Button(btnrow5, text="19%", font=("Verdana Bold italic", 22), relief=RAISED, border=0, fg="green",command=btn_divide_isclicked)
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)


root.mainloop()
