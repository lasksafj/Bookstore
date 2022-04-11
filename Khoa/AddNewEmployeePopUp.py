from tkinter import *
from PIL import Image, ImageTk

# Define delete function
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

# Create Tk instance
addEmployeeForm = Tk()
addEmployeeForm.resizable(0, 0)  # Lock screen
addEmployeeForm.title("Add New Employee")
addEmployeeForm.geometry("420x480")
addEmployeeForm.iconphoto(True, PhotoImage(file="logo.png"))

# Create labels
lastNameLabel = Label(addEmployeeForm, text="Last Name").grid(row=1,column=0,padx=20,pady=5)
lastName = Entry(addEmployeeForm, width=40)
firstNameLabel = Label(addEmployeeForm, text="First Name").grid(row=2,column=0,padx=20,pady=5)
firstName = Entry(addEmployeeForm, width=40)
addressLabel = Label(addEmployeeForm, text="Street Address").grid(row=3,column=0,padx=20,pady=5)
address = Entry(addEmployeeForm, width=40)
apartmentLabel = Label(addEmployeeForm, text="Apartment/Unit #").grid(row=4,column=0,padx=20,pady=5)
apartment = Entry(addEmployeeForm, width=40)
cityLabel = Label(addEmployeeForm, text="City").grid(row=5,column=0,padx=20,pady=5)
city = Entry(addEmployeeForm, width=40)
stateLabel = Label(addEmployeeForm, text="State").grid(row=6,column=0,padx=20,pady=5)
state = Entry(addEmployeeForm, width=40)
zipCodeLabel = Label(addEmployeeForm, text="ZIP").grid(row=7,column=0,padx=20,pady=5)
zipCode = Entry(addEmployeeForm, width=40)
phoneLabel = Label(addEmployeeForm, text="Phone").grid(row=8,column=0,padx=20,pady=5)
phone = Entry(addEmployeeForm, width=40)
emailLabel = Label(addEmployeeForm, text="E-mail Address").grid(row=9,column=0,padx=20,pady=5)
email = Entry(addEmployeeForm, width=40)
dateOfBirthLabel = Label(addEmployeeForm, text="Date of Birth").grid(row=10,column=0,padx=20,pady=5)
dateOfBirth = Entry(addEmployeeForm, width=40)
positionLabel = Label(addEmployeeForm, text="Position").grid(row=11,column=0,padx=20,pady=5)
position = Entry(addEmployeeForm, width=40)

# Create buttons
cancelButton = Button(addEmployeeForm, text="Cancel", command=addEmployeeForm.destroy)
cancelButton.grid(row=12,column=0,columnspan=2,padx=10,pady=5,ipadx=10,sticky="W")
clearButton = Button(addEmployeeForm, text="Clear", command=delete)
clearButton.grid(row=12,column=1,columnspan=2,pady=5,ipadx=10,sticky="W")
submitButton = Button(addEmployeeForm, text="Submit")
submitButton.grid(row=12,column=0,columnspan=2,padx=10,pady=20,ipadx=20,sticky="E")

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

# Go to next entry box if you press "Enter"
def go_to_next_entry(event, entry_list, this_index):
    next_index = (this_index + 1) % len(entry_list)
    entry_list[next_index].focus_set()

entries = [child for child in addEmployeeForm.winfo_children() if isinstance(child, Entry)]
for idx, entry in enumerate(entries):
    entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))

addEmployeeForm.mainloop()