from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

class AddNewEmployee(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(0, 0)  # Lock screen
        self.title("Add New Employee")
        self.geometry("420x480")
        self.iconphoto(True, PhotoImage(file="logo.png"))
    
    def showLabel(self):
        # Create labels
        lastNameLabel = Label(self, text="Last Name")
        firstNameLabel = Label(self, text="First Name")
        addressLabel = Label(self, text="Street Address")
        apartmentLabel = Label(self, text="Apartment/Unit #")
        cityLabel = Label(self, text="City")
        stateLabel = Label(self, text="State")
        zipCodeLabel = Label(self, text="ZIP")
        phoneLabel = Label(self, text="Phone")
        emailLabel = Label(self, text="E-mail Address")
        dateOfBirthLabel = Label(self, text="Date of Birth")
        positionLabel = Label(self, text="Position")

        # Labels grid
        lastNameLabel.grid(row=1,column=0,padx=20,pady=5)
        firstNameLabel.grid(row=2,column=0,padx=20,pady=5)
        addressLabel.grid(row=3,column=0,padx=20,pady=5)
        apartmentLabel.grid(row=4,column=0,padx=20,pady=5)
        cityLabel.grid(row=5,column=0,padx=20,pady=5)
        stateLabel.grid(row=6,column=0,padx=20,pady=5)
        zipCodeLabel.grid(row=7,column=0,padx=20,pady=5)
        phoneLabel.grid(row=8,column=0,padx=20,pady=5)
        emailLabel.grid(row=9,column=0,padx=20,pady=5)
        dateOfBirthLabel.grid(row=10,column=0,padx=20,pady=5)
        positionLabel.grid(row=11,column=0,padx=20,pady=5)


    def showTextbox(self):
        # Create text boxes
        lastName = Entry(self, width=40)
        firstName = Entry(self, width=40)
        address = Entry(self, width=40)
        apartment = Entry(self, width=40)
        city = Entry(self, width=40)
        state = Entry(self, width=40)
        zipCode = Entry(self, width=40)
        phone = Entry(self, width=40)
        email = Entry(self, width=40)
        dateOfBirth = Entry(self, width=40)
        position = Entry(self, width=40)

        # Text boxes grid
        lastName.grid(row=1,column=1)
        firstName.grid(row=2,column=1)
        address.grid(row=3,column=1)
        apartment.grid(row=4,column=1)
        city.grid(row=5,column=1)
        state.grid(row=6,column=1)
        zipCode.grid(row=7,column=1)
        phone.grid(row=8,column=1)
        email.grid(row=9,column=1)
        dateOfBirth.grid(row=10,column=1)
        position.grid(row=11,column=1)

    def showButton(self):
        # Create buttons
        cancelButton = Button(self, text="Cancel", command=self.destroy)
        cancelButton.grid(row=12,column=0,columnspan=2,padx=10,pady=5,ipadx=10,sticky="W")
        clearButton = Button(self, text="Clear")
        clearButton.grid(row=12,column=1,columnspan=2,pady=5,ipadx=10,sticky="W")
        submitButton = Button(self, text="Submit")
        submitButton.grid(row=12,column=0,columnspan=2,padx=10,pady=20,ipadx=20,sticky="E")

    def render(self):
        self.showLabel()
        self.showTextbox()
        self.showButton()

if __name__ == "__main__":
    app = AddNewEmployee()
    app.render()
    app.mainloop()