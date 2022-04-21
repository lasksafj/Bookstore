from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from turtle import width

class EditBook(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master, controller)
        self.controller = controller
        # self.render

    def buttonTop(self):
        # Creating a Label Wiglet
        self.frame1 = Frame(self, padx=5, pady=5)
        self.frame1.grid(row=2, column=1, columnspan=22, sticky="e")
        # frameWidth = self.frame1.winfo_screenwidth() * 23/25
        # print(frameWidth)
        # widthColumn = int(frameWidth/15)

        # Change Page button
        self.bookButton = Button(self.frame1, text="Books", width=20)
        self.customerButton = Button(self.frame1, text="Customer", width=20)
        self.employeeButton = Button(self.frame1, text="Employee", width=20)
        self.authorButton = Button(self.frame1, text="Author", width=20)

        # Show change page button
        self.bookButton.grid(row=2, column=1, sticky="e", padx=5, pady=5)
        self.customerButton.grid(row=2, column=2, sticky="e", padx=5, pady=5)
        self.employeeButton.grid(row=2, column=3, sticky="e", padx=5, pady=5)
        self.authorButton.grid(row=2, column=4, sticky="e", padx=5, pady=5)

    def searchBoxAndAdd(self):
        self.frame2 = Frame(self, padx=5, pady=5)
        self.frame2.grid(row=3, column=1, columnspan=22, sticky="e")
        # Search box
        self.searchBox = Entry(self.frame2, width=50,fg="blue", borderwidth=3)
        self.searchBox.grid(row=1, column=3, sticky="e", padx=5, pady=5)

        # Add button
        self.addButton = Button(self.frame2, text="Add New Book", width=20)
        self.addButton.grid(row=1, column=4, sticky="e", padx=5, pady=5)

    def rightClick(self):
        # creat mouse click
        self.rightClick = Menu(self, tearoff=False)

        def edit():
            pass
        def delete():
            pass
        def rightClickPopUp(e):
            self.rightClick.tk_popup(e.x_self, e.y_self)

        self.rightClick.add_command(label="Edit", command=edit)
        self.rightClick.add_command(label="Delete", command=delete)

        self.bind("<Button-3>", rightClickPopUp)

    def createTable(self):
        # Create Frame for list
        self.frame3 = tk.LabelFrame(self)
        self.frame3.grid(row=4, column=1, columnspan=30)
        frameWidth = self.frame3.winfo_screenwidth() * 23/25
        print(frameWidth)
        widthColumn = int(frameWidth/15)


        # Scrollbar
        table_scroll = Scrollbar(self.frame3)
        table_scroll.pack(side=RIGHT, fill=Y) ## fix with grid
        # table_scroll.grid(row=5, pady=20)

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

        # Add data test
        for i in range(0,5):
            self.table.insert(parent="",index="end", iid=i, text="", values=("ABCD1234", "asdrhgaedtrhg", "sarfgaer"))
        for i in range(6,20):
            self.table.insert(parent="",index="end", iid=i, text="", values=("GBDG6575", "asdrhgaedtrhg", "sarfgaer"))

        # Show
        self.table.pack() # fix with grid
        # self.table.grid(row=5, pady=20)

        self.rightClick = Menu(self.table, tearoff=False)

        def edit():
            pass
        def delete():
            pass
        def rightClickPopUp(e):
            self.rightClick.tk_popup(e.x_self.table, e.y_self.table)

        self.rightClick.add_command(label="Edit", command=edit)
        self.rightClick.add_command(label="Delete", command=delete)

        self.bind("<Button-3>", rightClickPopUp)

    # def scrollbarForTable(self):
        # Table Frame
        # table_frame = Frame(self)
        # table_frame.grid(row=4, column=1, padx=5, pady=5)

        # # Scrollbar
        # table_scroll = Scrollbar(self.table)
        # table_scroll.grid(column=side=RIGHT, fill=Y)
        #
        #
        # # Create table Frame
        # table = ttk.Treeview(self.table, yscrollcommand=table_scroll.set)
        # table.pack()
        #
        # # Configure the Scrollbar
        # table_scroll.config(command=table.yview)

    def editButton(self):
        # Creating a Label Wiglet
        self.frame4 = Frame(self, padx=10, pady=10)
        self.frame4.grid(row=5, column=2, columnspan=22, sticky="e")
        # frameWidth = self.frame3.winfo_screenwidth() * 23/25
        # print(frameWidth)
        # widthColumn = int(frameWidth/15)

        # Create button
        self.cancelButton = Button(self.frame4, text="Cancel", width=20)
        self.saveButton = Button(self.frame4, text="Save", width=20)

        # Shhow button onto the screen
        self.cancelButton.grid(row=1, column=3, sticky="e")
        self.saveButton.grid(row=1, column=4, sticky="e")

    def render(self):
        '''Create the grid of window with 10 rows and 25 columns'''
        for i in range(10):
            self.grid_rowconfigure(i, weight=1)
        for i in range(25):
            self.grid_columnconfigure(i, weight=1)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        font_size = screen_width/5

        store_label = tk.Label(self, text="Book List", font= font_size, bg='red')
        store_label.grid(row=0, column=1, sticky='nsew', rowspan=2, columnspan=25)
        # blank = tk.Label(self).grid(row=0, column=0)

        self.createTable()
        # self.scrollbarForTable()
        self.buttonTop()
        self.editButton()
        self.searchBoxAndAdd()
        # self.rightClick()


root = tk.Tk()
root.state('zoomed')
app = EditBook(root, controller={})
app.pack(fill="both", expand=True)
app.render()
app.mainloop()
