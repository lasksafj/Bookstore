from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Edit employee")
window.geometry("600x700")
window.iconphoto(True, PhotoImage(file="logo.png"))

f_name = Entry(window, width=30)
f_name.grid(row=0, column=1, padx=20)

window.mainloop()