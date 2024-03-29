from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
# from dbsql import * as db
import dbsql as db


class AddNewBook(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        # self.render()
        # ----
        self.con = db.create_connection("../bookstore.db")

    def popup(self):
        # Create Frame for list
        self.frame1 = Frame(self)
        self.frame1.grid(row=1, column=0, padx=10, pady=10)

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

    # def showTextbox(self):
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

    # def showButton(self):
        data = []
        # Create button
        clearButton = Button(self, text="Clear", pady=5, command=self.clear)
        saveButton = Button(self, text="Save", padx=10, pady=5, command=db.insert_db(self.con, "books", data))

        # Shhow button onto the screen
        clearButton.grid(row=15, column=1, sticky="e", ipadx=10, padx=50)
        saveButton.grid(row=15, column=1, sticky="e")

    def clear():
        # global bookID, title, author, publisher, publicationDate, edition, cost, suggestRetailPrice, condition, dateIn, dateOut
        bookID.delete(0, END)
        title.delete(0, END)
        author.delete(0, END)
        publisher.delete(0, END)
        publicationDate.delete(0, END)
        edition.delete(0, END)
        cost.delete(0, END)
        suggestRetailPrice.delete(0, END)
        condition.delete(0, END)
        sold.delete(0, END)
        dateIn.delete(0, END)
        dateOut.delete(0, END)




    def render(self):
        self.popup()
        # self.showTextbox()
        # self.showButton()


root = tk.Tk()
root.geometry("480x480")
app = AddNewBook(root, controller={})
app.pack(fill="both", expand=True)
app.render()
app.mainloop()
