from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from turtle import width
import dbsql as db
# import PopUpAddBook

class EditBook(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master, controller)
        self.controller = controller
        # self.render
        self.con = db.create_connection("../bookstore.db")
        #self.add()

    def buttonTop(self):
        # Creating Frame
        self.frame1 = Frame(self)
        self.frame1.grid(row=2, column=1, columnspan=22, sticky="e")

        # Switch Page button
        self.bookButton = Button(self.frame1, text="Books", width=20)
        self.customerButton = Button(self.frame1, text="Customer", width=20)
        self.employeeButton = Button(self.frame1, text="Employee", width=20)
        self.authorButton = Button(self.frame1, text="Author", width=20)

        # Show switch page button
        self.bookButton.grid(row=2, column=1, sticky="e")
        self.customerButton.grid(row=2, column=2, sticky="e")
        self.employeeButton.grid(row=2, column=3, sticky="e")
        self.authorButton.grid(row=2, column=4, sticky="e")

    def searchBoxAndAdd(self):
        # Create Frame
        self.frame2 = Frame(self)
        self.frame2.grid(row=3, column=1, columnspan=22, sticky="e")
        # Search box and Add button
        self.searchBox = Entry(self.frame2, width=50,fg="blue", borderwidth=3)
        self.addButton = Button(self.frame2, text="Add New Book", width=20)

        # Show search box and Add button
        self.searchBox.grid(row=1, column=3, sticky="e")
        self.addButton.grid(row=1, column=4, sticky="e")

    def createTable(self):
        # Create Frame for list
        self.frame3 = tk.LabelFrame(self, width=50)
        self.frame3.grid(row=4, column=1, columnspan=20)
        frameWidth = self.frame3.winfo_screenwidth()
        print(frameWidth)
        widthColumn = int(frameWidth/15)

        # Scrollbar
        table_scroll = Scrollbar(self.frame3)
        # table_scroll.pack(side=RIGHT, fill=Y)
        table_scroll.grid(row=5, column=1)

        # Create table
        self.table = ttk.Treeview(self.frame3, yscrollcommand=table_scroll.set)

        # Configure the Scrollbar
        table_scroll.config(command=self.table.yview)

        # define our columns
        self.table["columns"] = ("BOOK ID", "TITLE", "AUTHOR", "PUBLISHER", "PUBLICATION DATE", "EDITION", "COST", "SUG RETAIL PRICE", "CONDITION", "SOLD", "DATE IN", "DATE OUT", "DESCRIPTION")

        # Format column
        self.table.column("#0", width=0, minwidth=0)
        self.table.column("BOOK ID", anchor=CENTER, width=widthColumn)
        self.table.column("TITLE", anchor=W, width=widthColumn)
        self.table.column("AUTHOR", anchor=W, width=widthColumn)
        self.table.column("PUBLISHER", anchor=W, width=widthColumn)
        self.table.column("PUBLICATION DATE", anchor=W, width=widthColumn)
        self.table.column("EDITION", anchor=W, width=widthColumn)
        self.table.column("COST", anchor=E, width=widthColumn)
        self.table.column("SUG RETAIL PRICE", anchor=E, width=widthColumn)
        self.table.column("CONDITION", anchor=W, width=widthColumn)
        self.table.column("SOLD", anchor=W, width=widthColumn)
        self.table.column("DATE IN", anchor=W, width=widthColumn)
        self.table.column("DATE OUT", anchor=W, width=widthColumn)
        self.table.column("DESCRIPTION", anchor=W, width=widthColumn)

        # Create heading
        self.table.heading("#0", text="", anchor=CENTER)
        self.table.heading("BOOK ID", text="BOOK ID", anchor=CENTER)
        self.table.heading("TITLE", text="TITLE", anchor=CENTER)
        self.table.heading("AUTHOR", text="AUTHOR", anchor=CENTER)
        self.table.heading("PUBLISHER", text="PUBLISHER", anchor=CENTER)
        self.table.heading("PUBLICATION DATE", text="PUBLICATION DATE", anchor=CENTER)
        self.table.heading("EDITION", text="EDITION", anchor=CENTER)
        self.table.heading("COST", text="COST", anchor=CENTER)
        self.table.heading("SUG RETAIL PRICE", text="PRICE", anchor=CENTER)
        self.table.heading("CONDITION", text="CONDITION", anchor=CENTER)
        self.table.heading("SOLD", text="SOLD", anchor=CENTER)
        self.table.heading("DATE IN", text="DATE IN", anchor=CENTER)
        self.table.heading("DATE OUT", text="DATE OUT", anchor=CENTER)
        self.table.heading("DATE OUT", text="DATE OUT", anchor=CENTER)
        self.table.heading("DESCRIPTION", text="DESCRIPTION", anchor=CENTER)

        # # Add data test
        # for i in range(0,5):
        #     self.table.insert(parent="",index="end", iid=i, text="", values=("ABCD1234", "asdrhgaedtrhg", "sarfgaer"))
        # for i in range(6,20):
        #     self.table.insert(parent="",index="end", iid=i, text="", values=("GBDG6575", "asdrhgaedtrhg", "sarfgaer"))

        # Show
        self.table.grid(row=5, column=1)

    def render(self):
        '''Create the grid of window with 10 rows and 25 columns'''
        for i in range(30):
            self.grid_rowconfigure(i, weight=1)
        for i in range(50):
            self.grid_columnconfigure(i, weight=1)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        font_size = screen_width/5

        store_label = tk.Label(self, text="Book List", font= font_size, bg='gray')
        store_label.grid(row=0, column=1, sticky='nsew', rowspan=2, columnspan=25)
        # blank = tk.Label(self).grid(row=0, column=0)

        self.createTable()
        self.buttonTop()
        # self.editButton()
        self.searchBoxAndAdd()



root = tk.Tk()
root.state('zoomed')
app = EditBook(root, controller={})
app.pack(fill="both", expand=True)
app.render()
app.mainloop()
