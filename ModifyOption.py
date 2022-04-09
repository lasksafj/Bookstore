from tkinter import *
from PIL import Image, ImageTk

#class ModifyOption:
window = Tk()
window.title("Bookstore")
window.geometry("600x700")
window.iconphoto(True, PhotoImage(file="logo.png"))

# Create Button
backButton = Button(window, text="Back", padx=10, pady=5, fg="white", bg="blue")
blank = Label(window, text="")
bookButton = Button(window, text="Book", padx=20, pady=20, fg="white", bg="blue")
customerButton = Button(window, text="Customer", padx=20, pady=20, fg="white", bg="blue")
employeeButton = Button(window, text="Employee", padx=20, pady=20, fg="white", bg="blue")
authorButton = Button(window, text="Author", padx=20, pady=20, fg="white", bg="blue")

# Show button onto the screen
backButton.grid(row=0, column=0, sticky="w", padx=5, pady=5)
blank.grid(row=1, column=1)
blank.grid(row=1, column=2)
bookButton.grid(row=2, column=1, sticky="ew")
customerButton.grid(row=2, column=2, sticky="ew")
employeeButton.grid(row=3, column=1, sticky="ew")
authorButton.grid(row=3, column=2, sticky="ew")

window.mainloop()
