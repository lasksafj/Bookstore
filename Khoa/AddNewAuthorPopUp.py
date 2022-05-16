import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import dbsql

class AddNewAuthor(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.resizable(0, 0)  # Lock screen
        self.title("Add New Author")
        self.geometry("420x480")
        self.iconphoto(True, PhotoImage(file="logo.png"))


    def showLabel(self):
        # Create labels
        IDNumberLabel = Label(self, text="ID Number")
        lastNameLabel = Label(self, text="Last Name")
        firstNameLabel = Label(self, text="First Name")
        yearOfBirthLabel = Label(self, text="Year of Birth")
        yearOfDeathLabel = Label(self, text="Year of Death")
        descriptionLabel = Label(self, text="Description")

        # Labels grid
        IDNumberLabel.grid(row=1,column=0,padx=20,pady=10)
        lastNameLabel.grid(row=2,column=0,padx=20,pady=10)
        firstNameLabel.grid(row=3,column=0,padx=20,pady=10)
        yearOfBirthLabel.grid(row=4,column=0,padx=20,pady=10)
        yearOfDeathLabel.grid(row=5,column=0,padx=20,pady=10)
        descriptionLabel.grid(row=6,column=0,padx=20,pady=10)

    def showTextbox(self):
        # Create text boxes
        global IDNumber,lastName,firstName,yearOfBirth,yearOfDeath,description
        IDNumber = Entry(self, width=40)
        lastName = Entry(self, width=40)
        firstName = Entry(self, width=40)
        yearOfBirth = Entry(self, width=40)
        yearOfDeath = Entry(self, width=40)
        description = Text(self, width=30, height=6)

        # Text boxes grid
        IDNumber.grid(row=1,column=1)
        lastName.grid(row=2,column=1)
        firstName.grid(row=3,column=1)
        yearOfBirth.grid(row=4,column=1)
        yearOfDeath.grid(row=5,column=1)
        description.grid(row=6,column=1)
    
    def delete(self):
        IDNumber.delete(0, END)
        lastName.delete(0, END)
        firstName.delete(0, END)
        yearOfBirth.delete(0, END)
        yearOfDeath.delete(0, END)
        description.delete('1.0', END)

    def showButton(self):
        insert = [IDNumber,lastName,firstName,yearOfBirth,yearOfDeath,description]
        # Create buttons
        cancelButton = Button(self, text="Cancel", command=self.destroy)
        cancelButton.grid(row=12,column=0,columnspan=2,padx=10,pady=5,ipadx=10,sticky="W")
        clearButton = Button(self, text="Clear", command= self.delete)
        clearButton.grid(row=12,column=1,columnspan=2,pady=5,ipadx=10,sticky="W")
        submitButton = Button(self, text="Submit", command=dbsql.insert_db(dbsql.con, "author", insert))
        submitButton.grid(row=12,column=0,columnspan=2,padx=10,pady=20,ipadx=20,sticky="E")

    def render(self):
        self.showLabel()
        self.showTextbox()
        self.showButton()

if __name__ == "__main__":
    app = AddNewAuthor()
    app.render()
    app.mainloop()