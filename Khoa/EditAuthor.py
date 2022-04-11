from tkinter import *
from tkinter import ttk

# Create Tk instance
editAuthor = Tk()
editAuthor.title("Edit Author")
editAuthor.iconphoto(True, PhotoImage(file="logo.png"))
editAuthor.state("zoomed")

table = ttk.Treeview(editAuthor)
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



table.pack()
editAuthor.mainloop()