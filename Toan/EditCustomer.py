from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

class EditCustomer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Edit Customer")
        self.state("zoomed")
        self.res = 0;
        self.iconphoto(True, PhotoImage(file="logo.png"))

    def createTable(self):
        table = ttk.Treeview(self)

        # define our columns
        table["columns"] = ("CUSTOMER ID", "LAST NAME", "FIRST NAME", "PHONE NUMBER", "ADDRESS")

        # Format column
        table.column("#0", width=0, minwidth=0)
        table.column("CUSTOMER ID", anchor=CENTER, width=120)
        table.column("LAST NAME", anchor=W, width=120)
        table.column("FIRST NAME", anchor=W, width=120)
        table.column("PHONE NUMBER", anchor=W, width=120)
        table.column("ADDRESS", anchor=W, width=120)

        # Create heading
        table.heading("#0", text="", anchor=CENTER)
        table.heading("CUSTOMER ID", text="CUSTOMER ID", anchor=CENTER)
        table.heading("LAST NAME", text="LAST NAME", anchor=CENTER)
        table.heading("FIRST NAME", text="FIRST NAME", anchor=CENTER)
        table.heading("PHONE NUMBER", text="PHONE NUMBER", anchor=CENTER)
        table.heading("ADDRESS", text="ADDRESS", anchor=CENTER)

        # Show
        table.grid(row=8, pady=20)

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
        nameOfPage = Label(self, text="CUSTOMER", font=("Arial", 20))
        blank = Label(self, text="")


        # Showing it onto the screen
        nameOfPage.grid(row=0, column=0)
        blank.grid(row=1, column=0)
        blank.grid(row=2, column=0)
        blank.grid(row=4, column=0)
        blank.grid(row=5, column=0)


        # Change Page button
        bookButton = Button(self, text="Books", padx=10, pady=5)
        customerButton = Button(self, text="Customer", padx=10, pady=5)
        employeeButton = Button(self, text="Employee", padx=10, pady=5)
        authorButton = Button(self, text="Author", padx=10, pady=5)

        # Show change page button
        bookButton.grid(row=3, column=0, sticky="e", padx=240)
        customerButton.grid(row=3, column=0, sticky="e", padx=155)
        employeeButton.grid(row=3, column=0, sticky="e", padx=70)
        authorButton.grid(row=3, column=0, sticky="e")

    def searchBox(self):
        # Search box
        searchBox = Entry(self, width=50,fg="blue", borderwidth=3)
        searchBox.grid(row=6, column=0, sticky="e", ipadx=10, padx=120)

    def showButton(self):
        # Create button
        addButton = Button(self, text="Add New Customer", padx=10, pady=5)
        cancelButton = Button(self, text="Cancel", pady=5)
        saveButton = Button(self, text="Save", padx=10, pady=5)

        # Shhow button onto the screen
        addButton.grid(row=6, column=0, sticky="e")
        cancelButton.grid(row=15, column=0, sticky="e", ipadx=10, padx=60)
        saveButton.grid(row=15, column=0, sticky="e")

    # def rightClick():
    #     rightClick = Menu(self, tearoff=False)
    #
    #     def edit():
    #         pass
    #     def delete():
    #         pass
    #     def rightClickPopUp(e):
    # #         rightClick.tk_popup(e.x_self, e.y_self)
    #
    #     rightClick.add_command(label="Edit", command=edit)
    #     rightClick.add_command(label="Delete", command=delete)
    #
    #     self.bind("<Button-3>", rightClickPopUp)

    def render(self):
        self.createTable()
        #self.scrollbarForTable()
        self.buttonSwitchPage()
        self.searchBox()
        self.showButton()
        #self.rightClick()


if __name__ == "__main__":
    app = EditCustomer()
    app.render()
    app.mainloop()
