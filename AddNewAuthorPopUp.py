from tkinter import *
from PIL import Image, ImageTk

# Define delete function
def delete():
   IDNumber.delete(0, 'end')
   lastName.delete(0, 'end')
   firstName.delete(0, 'end')
   yearOfBirth.delete(0, 'end')
   yearOfDeath.delete(0, 'end')
   description.delete('1.0', 'end')

addAuthorForm = Tk()
addAuthorForm.resizable(0, 0)  # Lock screen
addAuthorForm.title("Add New Author")
addAuthorForm.geometry("420x480")
addAuthorForm.iconphoto(True, PhotoImage(file="logo.png"))

# Create labels
IDNumberLabel = Label(addAuthorForm, text="ID Number").grid(row=1,column=0,padx=20,pady=10)
IDNumber = Entry(addAuthorForm, width=40)
lastNameLabel = Label(addAuthorForm, text="Last Name").grid(row=2,column=0,padx=20,pady=10)
lastName = Entry(addAuthorForm, width=40)
firstNameLabel = Label(addAuthorForm, text="First Name").grid(row=3,column=0,padx=20,pady=10)
firstName = Entry(addAuthorForm, width=40)
yearOfBirthLabel = Label(addAuthorForm, text="Year of Birth").grid(row=4,column=0,padx=20,pady=10)
yearOfBirth = Entry(addAuthorForm, width=40)
yearOfDeathLabel = Label(addAuthorForm, text="Year of Death").grid(row=5,column=0,padx=20,pady=10)
yearOfDeath = Entry(addAuthorForm, width=40)
descriptionLabel = Label(addAuthorForm, text="Description").grid(row=6,column=0,padx=20,pady=10)
description = Text(addAuthorForm, width=30, height=6)

# Create buttons
cancelButton = Button(addAuthorForm, text="Cancel")
cancelButton.grid(row=12,column=0,columnspan=2,padx=10,pady=5,ipadx=10,sticky="W")
clearButton = Button(addAuthorForm, text="Clear", command=delete)
clearButton.grid(row=12,column=1,columnspan=2,pady=5,ipadx=10,sticky="W")
submitButton = Button(addAuthorForm, text="Submit")
submitButton.grid(row=12,column=0,columnspan=2,padx=10,pady=20,ipadx=20,sticky="E")

# Text boxes grid
IDNumber.grid(row=1,column=1)
lastName.grid(row=2,column=1)
firstName.grid(row=3,column=1)
yearOfBirth.grid(row=4,column=1)
yearOfDeath.grid(row=5,column=1)
description.grid(row=6,column=1)

addAuthorForm.mainloop()