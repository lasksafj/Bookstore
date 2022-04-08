from tkinter import *
from PIL import Image, ImageTk
# Employee, author

def delete():
   lastName.delete(0, 'end')
   firstName.delete(0, 'end')
   address.delete(0, 'end')
   apartment.delete(0, 'end')
   city.delete(0, 'end')
   state.delete(0, 'end')
   zipCode.delete(0, 'end')
   phone.delete(0, 'end')
   email.delete(0, 'end')
   dateOfBirth.delete(0, 'end')
   position.delete(0, 'end')

addForm = Tk()
addForm.resizable(0, 0)
addForm.title("Add New Employee")
addForm.geometry("450x550")
addForm.iconphoto(True, PhotoImage(file="logo.png"))

lastNameLabel = Label(addForm, text="Last Name").grid(row=1,column=0,padx=20,pady=5)
lastName = Entry(addForm, width=40)
firstNameLabel = Label(addForm, text="First Name").grid(row=2,column=0,padx=20,pady=5)
firstName = Entry(addForm, width=40)
addressLabel = Label(addForm, text="Street Address").grid(row=3,column=0,padx=20,pady=5)
address = Entry(addForm, width=40)
apartmentLabel = Label(addForm, text="Apartment/Unit #").grid(row=4,column=0,padx=20,pady=5)
apartment = Entry(addForm, width=40)
cityLabel = Label(addForm, text="City").grid(row=5,column=0,padx=20,pady=5)
city = Entry(addForm, width=40)
stateLabel = Label(addForm, text="State").grid(row=6,column=0,padx=20,pady=5)
state = Entry(addForm, width=40)
zipCodeLabel = Label(addForm, text="ZIP").grid(row=7,column=0,padx=20,pady=5)
zipCode = Entry(addForm, width=40)
phoneLabel = Label(addForm, text="Phone").grid(row=8,column=0,padx=20,pady=5)
phone = Entry(addForm, width=40)
emailLabel = Label(addForm, text="E-mail Address").grid(row=9,column=0,padx=20,pady=5)
email = Entry(addForm, width=40)
dateOfBirthLabel = Label(addForm, text="Date of Birth").grid(row=10,column=0,padx=20,pady=5)
dateOfBirth = Entry(addForm, width=40)
positionLabel = Label(addForm, text="Position").grid(row=11,column=0,padx=20,pady=5)
position = Entry(addForm, width=40)


submitButton = Button(addForm, text="Submit")
submitButton.grid(row=12,column=0,columnspan=2,padx=10,pady=20)

clearButton = Button(addForm, text="Clear", command=delete)
clearButton.grid(row=13,column=0,columnspan=2,pady=5)

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


#addForm.mainloop()