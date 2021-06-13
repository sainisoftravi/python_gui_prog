import tkinter.messagebox
from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Gst Calculator Converter")
window.geometry("400x300")
def gst_withvalue():

    item1 = (user_value.get())

    if item1.isdigit():
        textValue_gst = float(item1)*1.18
        t1.delete("1.0",END)
        z= t1.insert(END,textValue_gst)
        return TRUE
    else:
        tkinter.messagebox.showerror("Wrong Entry","Only Enter Number Only")
        return TRUE
    



def gst_withoutvalue():
    item1 = (user_value.get())

    if item1.isdigit():
        textValue_Wgst = float(item1) / 1.18
        t2.delete("1.0", END)
        z = t2.insert(END, textValue_Wgst)
        return TRUE
    else:
        tkinter.messagebox.showerror("Wrong Entry", "Only Enter Number Only")
        return TRUE

def clearFun():

    clearItem = tkinter.messagebox.askyesno("Clear Message","Kindly Click yes or No for Clear")
    if clearItem > 0:
        t1.delete("1.0", END)
        t2.delete("1.0", END)
        user_value.set("")
        return

def exitFun():
    iexit = tkinter.messagebox.askyesno("Exit Message","Confirm if you want to Exit")
    if iexit > 0:
        window.destroy()
        return

e1 = Label(window, text="Insert the Value",font="Times 14 bold italic",bg="Blue")
e1.grid(row=0,column=0,ipadx=12,ipady=10)
user_value= StringVar()
e2 = Entry(window,textvariable=user_value)
e2.grid(row=0,column=1,ipadx=12,ipady=10)

e3 = Label(window,text="With Gst",border=5,bg="green",font="Bold")
e3.grid(row=1,column=0,ipadx=12,ipady=10)
t1 = Text(window,height=3, width = 20)
t1.grid(row=2,column=0)

e4 = Label(window,text="Without Gst",border=5,bg="red",font="Bold")
e4.grid(row=1,column=1,ipadx=12,ipady=10)
t2 = Text(window,height=3, width = 20)
t2.grid(row=2,column=1)

b1 =Button(window,text="Convert in 18% GSt",font="Bold",activebackground="lightblue",command=gst_withvalue)
b1.grid(row=3,column=0)

b2 =Button(window,text="Convert Without GSt",font="Bold",command=gst_withoutvalue)
b2.grid(row=3,column=1)

b2 =Button(window,text="Clear",font="Bold",command=clearFun)
b2.grid(row=4,column=0)

b3 =Button(window,text="Exit",font="Bold",command=exitFun)
b3.grid(row=4,column=1)



window.mainloop()