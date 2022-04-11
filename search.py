from asyncore import compact_traceback
from multiprocessing.sharedctypes import Value
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from requests import delete
from setuptools import Command

class Search(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BOOKSTORE")
        self.geometry("400x500")
        # self.iconphoto(True, PhotoImage(file="icons8-bookstore-64.png"))

    def search_button(self):
        pass


    def clear(self):
        self.title_box.delete(0, END)
        self.iD_box.delete(0, END)
        self.author_box.delete(0, END)
        self.publisher_box.delete(0, END)
        self.year_box.delete(0, END)
        self.condition_box.current(0)
        self.category_box.current(0)
        self.status_box.current(0)

    def back(self):
        pass

    def searchBook(self):

        label = Label(self, text="Searching Box", font=("Helvatica", 20))
        label.grid(row=0, column=0, columnspan=2, pady=20)
        # Create Label
        title_label = tk.Label(self, text="Title")
        title_label.grid(row=1, column=0, padx= 10, sticky=W)
        iD_label = tk.Label(self, text="ID")
        iD_label.grid(row=2, column=0, padx= 10, sticky=W)
        author_label = tk.Label(self, text="Author")
        author_label.grid(row=3, column=0, padx= 10, sticky=W)
        publisher_label = tk.Label(self, text="Publisher")
        publisher_label.grid(row=4, column=0, padx= 10, sticky=W)
        year_label = tk.Label(self, text="Year")
        year_label.grid(row=5, column=0, padx= 10, sticky=W)
        condition_label = tk.Label(self, text="Condition")
        condition_label.grid(row=6, column=0, padx= 10, sticky=W)
        category_label = tk.Label(self, text="Category")
        category_label.grid(row=7, column=0, padx= 10, sticky=W)
        status_label = tk.Label(self, text="Status")
        status_label.grid(row=8, column=0, padx= 10, sticky=W)

        # Create Entry Boxes
        self.title_box = tk.Entry(self, width=40)
        self.title_box.grid(row=1, column=1, pady=10)
        self.iD_box = tk.Entry(self, width=40)
        self.iD_box.grid(row=2, column=1, pady=10)
        self.author_box = tk.Entry(self, width=40)
        self.author_box.grid(row=3, column=1, pady=10)
        self.publisher_box = tk.Entry(self, width=40)
        self.publisher_box.grid(row=4, column=1, pady=10)
        self.year_box = tk.Entry(self, width=40)
        self.year_box.grid(row=5, column=1, pady=10)

        self.condition_box = ttk.Combobox(self, values=["Choose", "New", "Good", "Bad"], width=37)
        self.condition_box.current(0)
        self.condition_box.grid(row=6, column=1, pady=10)
        self.category_box = ttk.Combobox(self, values=["Choose", "Science", "Fiction", "Novel"], width=37)
        self.category_box.current(0)
        self.category_box.grid(row=7, column=1, pady=10)
        self.status_box = ttk.Combobox(self, values=["Choose", "Available", "Sold"], width=37)
        self.status_box.current(0)
        self.status_box.grid(row=8, column=1, pady=10)

        #Create Buttons
        search_button = tk.Button(self, text="Search...", width=15, command=self.search_button)
        search_button.grid(row=9, column=0)

        delete_button = tk.Button(self, text="Clear Fields", command=self.clear)
        delete_button.grid(row=9, column=1)

        back_button = tk.Button(self, text="<<", command=self.back)
        back_button.grid(row=10, column=0, pady=20, sticky=W)
        
        


if __name__ == "__main__":
    app = Search()
    app.searchBook()
    app.mainloop()