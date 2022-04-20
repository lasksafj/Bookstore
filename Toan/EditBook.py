from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

class EditBook(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Books")
        self.state("zoomed")
        self.res = 0;
        self.iconphoto(True, PhotoImage(file="logo.png"))

    def createTable(self):
        # Create Frame for list
        self.frameList = LabelFrame(self, padx=10, pady=10)
        self.frameList.pack(padx=10, pady=10)
        # Create table
        self.table = ttk.Treeview(self.frameList)

        # define our columns
        self.table["columns"] = ("BOOK ID", "TITLE", "AUTHOR", "PUBLISHER", "PUBLICATION DATE", "EDITION", "COST", "SUG RETAIL PRICE", "CONDITION", "SOLD", "DATE IN", "DATE OUT", "DESCRIPTION")

        # Format column
        self.table.column("#0", width=0, minwidth=0)
        self.table.column("BOOK ID", anchor=CENTER, width=120)
        self.table.column("TITLE", anchor=W, width=120)
        self.table.column("AUTHOR", anchor=W, width=120)
        self.table.column("PUBLISHER", anchor=W, width=120)
        self.table.column("PUBLICATION DATE", anchor=W, width=120)
        self.table.column("EDITION", anchor=W, width=120)
        self.table.column("COST", anchor=E, width=120)
        self.table.column("SUG RETAIL PRICE", anchor=E, width=120)
        self.table.column("CONDITION", anchor=W, width=120)
        self.table.column("SOLD", anchor=W, width=120)
        self.table.column("DATE IN", anchor=W, width=120)
        self.table.column("DATE OUT", anchor=W, width=120)
        self.table.column("DESCRIPTION", anchor=W, width=120)

        # Create heading
        self.table.heading("#0", text="", anchor=CENTER)
        self.table.heading("BOOK ID", text="BOOK ID", anchor=CENTER)
        self.table.heading("TITLE", text="TITLE", anchor=CENTER)
        self.table.heading("AUTHOR", text="AUTHOR", anchor=CENTER)
        self.table.heading("PUBLISHER", text="PUBLISHER", anchor=CENTER)
        self.table.heading("PUBLICATION DATE", text="PUBLICATION DATE", anchor=CENTER)
        self.table.heading("EDITION", text="EDITION", anchor=CENTER)
        self.table.heading("COST", text="COST", anchor=CENTER)
        self.table.heading("SUG RETAIL PRICE", text="SUG RETAIL PRICE", anchor=CENTER)
        self.table.heading("CONDITION", text="CONDITION", anchor=CENTER)
        self.table.heading("SOLD", text="SOLD", anchor=CENTER)
        self.table.heading("DATE IN", text="DATE IN", anchor=CENTER)
        self.table.heading("DATE OUT", text="DATE OUT", anchor=CENTER)
        self.table.heading("DATE OUT", text="DATE OUT", anchor=CENTER)
        self.table.heading("DESCRIPTION", text="DESCRIPTION", anchor=CENTER)

        # Add data test
        for i in range(0,100):
            self.table.insert(parent="",index="end", iid=i, text="", values=("ABCD1234", "asdrhgaedtrhg", "sarfgaer"))

        # Show
        self.table.grid(row=8, pady=20)

        # creat mouse click
        self.bind("<Button-3>", self.rightClick)

    # def scrollbarForTable(self):
    #     # Table Frame
    #     table_frame = Frame(self)
    #     table_frame.pack(pady=20)
    #
    #     # Scrollbar
    #     table_scroll = Scrollbar(table_frame)
    #     table_scroll.pack(side=RIGHT, fill=Y)
    #
    #
    #     # Create table Frame
    #     table = ttk.Treeview(table_frame, yscrollcommand=table_scroll.set)
    #     table.pack()
    #
    #     # Configure the Scrollbar
    #     table_scroll.config(command=table.yview)

    def buttonSwitchPage(self):
        # Creating a Label Wiglet
        self.frameButton = LabelFrame(self, padx=10, pady=10)
        self.frameButton.pack(padx=10, pady=10)

        # Change Page button
        self.bookButton = Button(self, text="Books", padx=10, pady=5)
        self.customerButton = Button(self, text="Customer", padx=10, pady=5)
        self.employeeButton = Button(self, text="Employee", padx=10, pady=5)
        self.authorButton = Button(self, text="Author", padx=10, pady=5)

        # Show change page button
        self.bookButton.grid(row=3, column=0, sticky="e", padx=240)
        self.customerButton.grid(row=3, column=0, sticky="e", padx=155)
        self.employeeButton.grid(row=3, column=0, sticky="e", padx=70)
        self.authorButton.grid(row=3, column=0, sticky="e")

    def searchBox(self):
        # Search box
        self.searchBox = Entry(self, width=50,fg="blue", borderwidth=3)
        self.searchBox.grid(row=6, column=0, sticky="e", ipadx=10, padx=120)

    def showButton(self):
        # Create button
        self.addButton = Button(self, text="Add New Book", padx=10, pady=5)
        self.cancelButton = Button(self, text="Cancel", pady=5)
        self.saveButton = Button(self, text="Save", padx=10, pady=5)

        # Shhow button onto the screen
        self.addButton.grid(row=6, column=0, sticky="e")
        self.cancelButton.grid(row=15, column=0, sticky="e", ipadx=10, padx=60)
        self.saveButton.grid(row=15, column=0, sticky="e")

    def rightClick():
        self.rightClick = Menu(self, tearoff=False)

        def edit():
            pass
        def delete():
            pass
        # def rightClickPopUp(e):
        #      rightClick.tk_popup(e.x_self, e.y_self)

        self.rightClick.add_command(label="Edit", command=edit)
        self.rightClick.add_command(label="Delete", command=delete)

        # self.bind("<Button-3>", rightClickPopUp)

    def render(self):
        self.createTable()
        #self.scrollbarForTable()
        self.buttonSwitchPage()
        self.searchBox()
        self.showButton()
        self.rightClick()


if __name__ == "__main__":
    app = EditBook()
    app.render()
    app.mainloop()
