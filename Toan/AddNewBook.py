from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class AddNewBook(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Add New Book")
        self.state("zoomed")
        self.res = 0;
        self.iconphoto(True, PhotoImage(file="logo.png"))

    def showLabel(self):
        # Create text box label
        nameOfPage = Label(self, text="Add New Book")
        blank = Label(self, text="")
        bookID = Label(self, text="BOOK ID")
        title = Label(self, text="TITLE")
        author = Label(self, text="AUTHOR")
        publisher = Label(self, text="PUBLISHER")
        publicationDate = Label(self, text="PUBLICATION DATE")
        edition = Label(self, text="EDITION")
        cost = Label(self, text="COST")
        suggestRetailPrice = Label(self, text="SUG RETAIL PRICE")
        condition = Label(self, text="CONDITION")
        sold = Label(self, text="SOLD")
        dateIn = Label(self, text="DATE IN")
        dateOut = Label(self, text="DATE OUT")

        # Showing label onto the screen
        nameOfPage.grid(row=0, column=1)
        blank.grid(row=1, column=0)
        blank.grid(row=2, column=0)
        bookID.grid(row=3, column=0, sticky="w", padx=10)
        title.grid(row=4, column=0, sticky="w", padx=10)
        author.grid(row=5, column=0, sticky="w", padx=10)
        publisher.grid(row=6, column=0, sticky="w", padx=10)
        publicationDate.grid(row=7, column=0, sticky="w", padx=10)
        edition.grid(row=8, column=0, sticky="w", padx=10)
        cost.grid(row=9, column=0, sticky="w", padx=10)
        suggestRetailPrice.grid(row=10, column=0, sticky="w", padx=10)
        condition.grid(row=11, column=0, sticky="w", padx=10)
        sold.grid(row=12, column=0, sticky="w", padx=10)
        dateIn.grid(row=13, column=0, sticky="w", padx=10)
        dateOut.grid(row=14, column=0, sticky="w", padx=10)

    def showTextbox(self):
        # Create text box entry
        bookID = Entry(self, width=50, fg="blue", borderwidth=3, state=DISABLED)
        title = Entry(self, width=50, fg="blue", borderwidth=3)
        author = Entry(self, width=50, fg="blue", borderwidth=3)
        publisher = Entry(self, width=50, fg="blue", borderwidth=3)
        publicationDate = Entry(self, width=50, fg="blue", borderwidth=3)
        edition = Entry(self, width=50, fg="blue", borderwidth=3)
        cost = Entry(self, width=50, fg="blue", borderwidth=3)
        suggestRetailPrice = Entry(self, width=50, fg="blue", borderwidth=3)
        condition = Entry(self, width=50, fg="blue", borderwidth=3)
        sold = Entry(self, width=50, fg="blue", borderwidth=3)
        dateIn = Entry(self, width=50, fg="blue", borderwidth=3)
        dateOut = Entry(self, width=50, fg="blue", borderwidth=3)

        # Show entry onto the screen
        bookID.grid(row=3, column=1)
        title.grid(row=4, column=1)
        author.grid(row=5, column=1)
        publisher.grid(row=6, column=1)
        publicationDate.grid(row=7, column=1)
        edition.grid(row=8, column=1)
        cost.grid(row=9, column=1)
        suggestRetailPrice.grid(row=10, column=1)
        condition.grid(row=11, column=1)
        sold.grid(row=12, column=1)
        dateIn.grid(row=13, column=1)
        dateOut.grid(row=14, column=1)

        # Insert comment for entry
        title.insert(4, "Enter title of book")
    def showButton(self):
        # Create button
        cancelButton = Button(self, text="Cancel", pady=5)
        saveButton = Button(self, text="Save", padx=10, pady=5)

        # Shhow button onto the screen
        cancelButton.grid(row=15, column=1, sticky="e", ipadx=10, padx=50)
        saveButton.grid(row=15, column=1, sticky="e")


    def render(self):
        self.showLabel()
        self.showTextbox()
        self.showButton()



if __name__ == "__main__":
    app = AddNewBook()
    app.render()
    app.mainloop()
