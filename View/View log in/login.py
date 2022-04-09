from tkinter import *
from tkinter import messagebox

def login():
    username = e1.get()
    password = e2.get()
    print(username)
    print(password)

    if username == "" and password == "":
        messagebox.showinfo("", "Blank Not Allowed")

    elif username == "annieh195" and password == "Anhhuynh190500":
        messagebox.showinfo("", "Login Success")

    else:
        messagebox.showinfo("", "Incorrect username or password")

window = Tk()
window.geometry("300x200")
global e1
global e2
Label(window, text="Username", font=("Arial",12)).place(x=10, y=10)
Label(window, text="Password", font=("Arial",12)).place(x=10, y=40)

e1 = Entry(window, font=("Arial",12))
e1.place(x=100, y=10)

e2 = Entry(window, font=("Arial",12), show="*")
e2.place(x=100, y=40)

login_button = Button(window,text="login",command=login)
login_button.pack(side=BOTTOM)

window.mainloop()