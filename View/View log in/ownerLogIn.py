from tkinter import *
from tkinter import messagebox

def owner():


window = Tk()
window.geometry("300x200")
global e1
global e2

e1 = Entry(window, font=("Arial",12))
e1.place(x=100, y=10)

e2 = Entry(window, font=("Arial",12), show="*")
e2.place(x=100, y=40)

login_button = Button(window,text="login",command=login)
login_button.pack(side=BOTTOM)

window.mainloop()