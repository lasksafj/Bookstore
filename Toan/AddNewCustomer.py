from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class AddNewCustomer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Add New Customer")
        self.state("zoomed")
        self.res = 0;
        self.iconphoto(True, PhotoImage(file="logo.png"))

    def showLabel(self):
        # Create text box label
        nameOfPage = Label(self, text="Add New Customer")
        blank = Label(self, text="")
        customerID = Label(self, text="CUSTOMER ID")
        lastName = Label(self, text="LAST NAME")
        firstName = Label(self, text="FIRST NAME")
        phoneNumber = Label(self, text="PHONE NUMBER")
        address = Label(self, text="ADDRESS")

        # Showing label onto the screen
        nameOfPage.grid(row=0, column=1)
        blank.grid(row=1, column=0)
        blank.grid(row=2, column=0)
        customerID.grid(row=3, column=0, sticky="w", padx=10)
        lastName.grid(row=4, column=0, sticky="w", padx=10)
        firstName.grid(row=5, column=0, sticky="w", padx=10)
        phoneNumber.grid(row=6, column=0, sticky="w", padx=10)
        address.grid(row=7, column=0, sticky="w", padx=10)

    def showTextbox(self):
        # Create text box entry
        customerID = Entry(self, width=50, fg="blue", borderwidth=3, state=DISABLED)
        lastName = Entry(self, width=50, fg="blue", borderwidth=3)
        firstName = Entry(self, width=50, fg="blue", borderwidth=3)
        phoneNumber = Entry(self, width=50, fg="blue", borderwidth=3)
        address = Entry(self, width=50, fg="blue", borderwidth=3)

        # Show entry onto the screen
        customerID.grid(row=3, column=1)
        lastName.grid(row=4, column=1)
        firstName.grid(row=5, column=1)
        phoneNumber.grid(row=6, column=1)
        address.grid(row=7, column=1)

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
    app = AddNewCustomer()
    app.render()
    app.mainloop()
