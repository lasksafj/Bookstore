from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class ModifyOption(tk.Frame):
    def __init__(self):
        super().__init__()
        self.title("Modify Option")
        self.state("zoomed")
        self.res = 0;
        self.iconphoto(True, PhotoImage(file="logo.png"))

    def showButton(self):
        # Create button
        backButton = Button(self, text="Back", font=("Arial", 20), padx=10, pady=5, fg="white", bg="blue")
        blank = Label(self, text="")
        bookButton = Button(self, text="Book", font=("Arial", 20), padx=20, pady=20, fg="white", bg="blue")
        customerButton = Button(self, text="Customer", font=("Arial", 20), padx=20, pady=20, fg="white", bg="blue")
        employeeButton = Button(self, text="Employee", font=("Arial", 20), padx=20, pady=20, fg="white", bg="blue")
        authorButton = Button(self, text="Author", font=("Arial", 20), padx=20, pady=20, fg="white", bg="blue")

        # Show button onto the screen
        backButton.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        blank.grid(row=1, column=1)
        blank.grid(row=1, column=2)
        bookButton.grid(row=2, column=1, sticky="ew")
        customerButton.grid(row=2, column=2, sticky="ew")
        employeeButton.grid(row=3, column=1, sticky="ew")
        authorButton.grid(row=3, column=2, sticky="ew")

    def render(self):
        self.showButton()


if __name__ == "__main__":
    app = ModifyOption()
    app.render()
    app.mainloop()
