from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Bookstore")
window.geometry("600x700")
window.iconphoto(True, PhotoImage(file="logo.png"))



image1 = ImageTk.PhotoImage(Image.open('background.png'))
back_ground = Label(window, image=image1)
back_ground.place(x=0, y=0)

frame = LabelFrame(window, text="Bookstore", padx=5, pady=5)
frame.pack(padx=10, pady=10)

label = Label(frame, text="WELLCOME TO BOOKSTORE APP", fg="red")
label.config(font=("Helvatical bold", 20))
label.pack(pady=20)



window.mainloop()
