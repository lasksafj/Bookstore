from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

class EditEmployee(tk.Tk):

    # Create Tk instance
    def __init__(self):
        super().__init__()
        self.title("Edit Employee")
        self.state("zoomed")
        self.res = 0
        self.iconphoto(True, PhotoImage(file="logo.png"))

    def createTable(self):
        table = ttk.Treeview(self)
        table["columns"] = ("Last Name", "First Name", "Street Address", "Apartment/Unit #", "City", "State", "ZIP", "Phone", "E-mail Address", "Date of Birth", "Position")

        table.column("#0", width=0, minwidth=0)
        table.heading("#0", text="")
        table.column("Last Name", anchor=W, width=100)
        table.heading("Last Name", text="Last Name",anchor=CENTER)
        table.column("First Name", anchor=W, width=100)
        table.heading("First Name", text="First Name",anchor=CENTER)
        table.column("Street Address", anchor=W, width=155)
        table.heading("Street Address", text="Street Address",anchor=CENTER)
        table.column("Apartment/Unit #", anchor=W, width=120)
        table.heading("Apartment/Unit #", text="Apartment/Unit #",anchor=CENTER)
        table.column("City", anchor=W, width=120)
        table.heading("City", text="City",anchor=CENTER)
        table.column("State", anchor=W, width=100)
        table.heading("State", text="State",anchor=CENTER)
        table.column("City", anchor=W, width=120)
        table.heading("City", text="City",anchor=CENTER)
        table.column("ZIP", anchor=W, width=100)
        table.heading("ZIP", text="ZIP",anchor=CENTER)
        table.column("Phone", anchor=W, width=120)
        table.heading("Phone", text="Phone",anchor=CENTER)
        table.column("E-mail Address", anchor=W, width=120)
        table.heading("E-mail Address", text="E-mail Address",anchor=CENTER)
        table.column("Date of Birth", anchor=W, width=120)
        table.heading("Date of Birth", text="Date of Birth",anchor=CENTER)
        table.column("Position", anchor=W, width=120)
        table.heading("Position", text="Position",anchor=CENTER)

        table.grid(row=8, pady=20)

    def buttonSwitchPage(self):
        # Creating a Label Wiglet
        nameOfPage = Label(self, text="EMPLOYEE", font=("Arial", 20))
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

    def searchBox(self):
        # Search box
        searchBox = Entry(self, width=50,fg="blue", borderwidth=3)
        searchBox.grid(row=6, column=0, sticky="e", ipadx=10, padx=120)

    def showButton(self):
        # Create button
        addButton = Button(self, text="Add New Employee", padx=10, pady=5)
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
    app = EditEmployee()
    app.render()
    app.mainloop()
