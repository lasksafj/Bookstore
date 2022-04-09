from tkinter import *
from tkinter import ttk

# Create Tk instance
editEmployee = Tk()
editEmployee.title("Edit Author")
editEmployee.iconphoto(True, PhotoImage(file="logo.png"))
editEmployee.state("zoomed")

table = ttk.Treeview(editEmployee)
table["columns"] = ("Last Name", "First Name", "Street Address", "Apartment/Unit #", "City", "State", "ZIP", "Phone", "E-mail Address", "Date of Birth", "Position")

table.column("#0", width=0, minwidth=0)
table.heading("#0", text="")
table.column("Last Name", anchor=W, width=150)
table.heading("Last Name", text="Last Name",anchor=CENTER)
table.column("First Name", anchor=W, width=150)
table.heading("First Name", text="First Name",anchor=CENTER)
table.column("Street Address", anchor=W, width=150)
table.heading("Street Address", text="Street Address",anchor=CENTER)
table.column("Apartment/Unit #", anchor=W, width=150)
table.heading("Apartment/Unit #", text="Apartment/Unit #",anchor=CENTER)
table.column("City", anchor=W, width=150)
table.heading("City", text="City",anchor=CENTER)
table.column("State", anchor=W, width=150)
table.heading("State", text="State",anchor=CENTER)
table.column("City", anchor=W, width=150)
table.heading("City", text="City",anchor=CENTER)
table.column("ZIP", anchor=W, width=150)
table.heading("ZIP", text="ZIP",anchor=CENTER)
table.column("Phone", anchor=W, width=150)
table.heading("Phone", text="Phone",anchor=CENTER)
table.column("E-mail Address", anchor=W, width=150)
table.heading("E-mail Address", text="E-mail Address",anchor=CENTER)
table.column("Date of Birth", anchor=W, width=150)
table.heading("Date of Birth", text="Date of Birth",anchor=CENTER)
table.column("Position", anchor=W, width=150)
table.heading("Position", text="Position",anchor=CENTER)


table.pack()
editEmployee.mainloop()