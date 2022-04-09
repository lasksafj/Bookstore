from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

window = Tk()
window.title("Bookstore")
window.geometry("600x700")
window.iconphoto(True, PhotoImage(file="logo.png"))

table = ttk.Treeview(window)

# define our columns
table["columns"] = ("BOOK ID", "TITLE", "AUTHOR", "PUBLISHER", "PUBLICATION DATE", "EDITION", "COST", "SUG RETAIL PRICE", "CONDITION", "SOLD", "DATE IN", "DATE OUT")

# Format column
table.column("#0", width=0, minwidth=0)
table.column("BOOK ID", anchor=CENTER, width=120)
table.column("TITLE", anchor=W, width=120)
table.column("AUTHOR", anchor=W, width=120)
table.column("PUBLISHER", anchor=W, width=120)
table.column("PUBLICATION DATE", anchor=W, width=120)
table.column("EDITION", anchor=W, width=120)
table.column("COST", anchor=E, width=120)
table.column("SUG RETAIL PRICE", anchor=E, width=120)
table.column("CONDITION", anchor=W, width=120)
table.column("SOLD", anchor=W, width=120)
table.column("DATE IN", anchor=W, width=120)
table.column("DATE OUT", anchor=W, width=120)

# Create heading
table.heading("#0", text="", anchor=CENTER)
table.heading("BOOK ID", text="BOOK ID", anchor=CENTER)
table.heading("TITLE", text="TITLE", anchor=CENTER)
table.heading("AUTHOR", text="AUTHOR", anchor=CENTER)
table.heading("PUBLISHER", text="PUBLISHER", anchor=CENTER)
table.heading("PUBLICATION DATE", text="PUBLICATION DATE", anchor=CENTER)
table.heading("EDITION", text="EDITION", anchor=CENTER)
table.heading("COST", text="COST", anchor=CENTER)
table.heading("SUG RETAIL PRICE", text="SUG RETAIL PRICE", anchor=CENTER)
table.heading("CONDITION", text="CONDITION", anchor=CENTER)
table.heading("SOLD", text="SOLD", anchor=CENTER)
table.heading("DATE IN", text="DATE IN", anchor=CENTER)
table.heading("DATE OUT", text="DATE OUT", anchor=CENTER)

# Add data test
for i in range(0,100):
    table.insert(parent="",index="end", iid=i, text="", values=("ABCD1234", "asdrhgaedtrhg", "sarfgaer"))


# Show
table.grid(row=8, pady=20)

# # Table Frame
# table_frame = Frame(window)
# table_frame.pack(pady=20)
#
# # Scrollbar
# table_scroll = Scrollbar(table_frame)
# table_scroll.pack(side=RIGHT, fill=Y)
#
#
# # Create table Frame
# table = ttk.Treeview(table_frame, yscrollcommand=table_scroll.set)
# table.pack()
#
# # Configure the Scrollbar
# table_scroll.config(command=table.yview)

# Creating a Label Wiglet
nameOfPage = Label(window, text="BOOKS")
blank = Label(window, text="")


# Showing it onto the screen
nameOfPage.grid(row=0, column=0)
blank.grid(row=1, column=0)
blank.grid(row=2, column=0)
blank.grid(row=4, column=0)
blank.grid(row=5, column=0)


# Change Page button
bookButton = Button(window, text="Books", padx=10, pady=5)
customerButton = Button(window, text="Customer", padx=10, pady=5)
employeeButton = Button(window, text="Employee", padx=10, pady=5)
authorButton = Button(window, text="Author", padx=10, pady=5)

# Show change page button
bookButton.grid(row=3, column=0, sticky="e", padx=240)
customerButton.grid(row=3, column=0, sticky="e", padx=155)
employeeButton.grid(row=3, column=0, sticky="e", padx=70)
authorButton.grid(row=3, column=0, sticky="e")

# Search box
searchBox = Entry(window, width=50,fg="blue", borderwidth=3)
searchBox.grid(row=6, column=0, sticky="e", ipadx=10, padx=120)

# Create button
addButton = Button(window, text="Add New Book", padx=10, pady=5)
cancelButton = Button(window, text="Cancel", pady=5)
saveButton = Button(window, text="Save", padx=10, pady=5)

# Shhow button onto the screen
addButton.grid(row=6, column=0, sticky="e")
cancelButton.grid(row=15, column=0, sticky="e", ipadx=10, padx=60)
saveButton.grid(row=15, column=0, sticky="e")



window.mainloop()
