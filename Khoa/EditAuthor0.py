from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import AddNewAuthorPopUp

class EditAuthor(tk.Tk):

    # Create Tk instance
    def __init__(self):
        super().__init__()
        self.title("Edit Author")
        self.state("zoomed")
        self.res = 0
        self.iconphoto(True, PhotoImage(file="logo.png"))

    def createTable(self):
        table = ttk.Treeview(self)
        table["columns"] = ("ID Number", "Last Name", "First Name", "Year of Birth", "Year of Death", "Description")

        table.column("#0", width=0, minwidth=0)
        table.heading("#0", text="")
        table.column("ID Number", anchor=W, width=150)
        table.heading("ID Number", text="ID Number",anchor=CENTER)
        table.column("Last Name", anchor=W, width=150)
        table.heading("Last Name", text="Last Name",anchor=CENTER)
        table.column("First Name", anchor=W, width=150)
        table.heading("First Name", text="First Name",anchor=CENTER)
        table.column("Year of Birth", anchor=W, width=150)
        table.heading("Year of Birth", text="Year of Birth",anchor=CENTER)
        table.column("Year of Death", anchor=W, width=150)
        table.heading("Year of Death", text="Year of Death",anchor=CENTER)
        table.column("Description", anchor=W, width=500)
        table.heading("Description", text="Description",anchor=CENTER)

        table.grid(row=8, pady=20)

    def buttonSwitchPage(self):
        # Creating a Label Wiglet
        nameOfPage = Label(self, text="AUTHOR", font=("Arial", 20))
        blank = Label(self, text="")


        # Showing it onto the screen
        nameOfPage.grid(row=0, column=0)
        blank.grid(row=1, column=0)
        blank.grid(row=2, column=0)
        blank.grid(row=4, column=0)
        blank.grid(row=5, column=0)

        # Change Page button
        bookButton = Button(self, text="Books", padx=10, pady=5)
        customerButton = Button(self, text="Customer", padx=10, pady=5)
        employeeButton = Button(self, text="Employee", padx=10, pady=5)
        authorButton = Button(self, text="Author", padx=10, pady=5)

        # Show change page button
        bookButton.grid(row=3, column=0, sticky="e", padx=240)
        customerButton.grid(row=3, column=0, sticky="e", padx=155)
        employeeButton.grid(row=3, column=0, sticky="e", padx=70)
        authorButton.grid(row=3, column=0, sticky="e")

    #def searchBox(self):
        # Search box
        #searchBox = Entry(self, width=50,fg="blue", borderwidth=3)
        #searchBox.grid(row=6, column=0, sticky="e", ipadx=10, padx=120)
    
    def open_window():
        window = AddNewAuthor(self)
        window.grab_set()
    
    def showButton(self):
        # Create button
        addButton = Button(self, text="Add New Author", padx=10, pady=5)
        cancelButton = Button(self, text="Cancel", command=self.destroy, pady=5)
        saveButton = Button(self, text="Save", padx=10, pady=5)

        # Shhow button onto the screen
        addButton.grid(row=6, column=0, sticky="e")
        cancelButton.grid(row=15, column=0, sticky="e", ipadx=10, padx=60)
        saveButton.grid(row=15, column=0, sticky="e")

    def render(self):
        self.createTable()
        self.buttonSwitchPage()
        self.searchBox()
        self.showButton()


if __name__ == "__main__":
    app = EditAuthor()
    app.render()
    app.mainloop()
