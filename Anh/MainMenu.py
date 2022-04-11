import tkinter as tk
from tkinter import ttk
# from CreateAccount import CreateAccount


class MainMenu(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        # self.master = master
        # self.master.title("Bookstore")

        self.controller = controller
        # self.controller.state("zoomed")
        self.render()

    def render(self):
        # configure the grid of the frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=2)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # widget for resizing at the corner
        ttk.Sizegrip(self).grid(row=3, column=2, sticky=tk.SE)

        # grid the frame
        # self.grid(row=0, column=0)

        # fill the window with the frame
        # self.pack(expand=1, fill=tk.BOTH)

        # creating widgets
        search_button = tk.Button(self, text="Search and Order", font=("Arial", 30),
                                  command=lambda: self.search_and_order_button())
        search_button.grid(row=0, columnspan=2, sticky="NSEW", padx=10, pady=10)

        create_button = tk.Button(self, text="Create Account", font=("Arial", 20),
                                  command=lambda: self.create_account_button())
        create_button.grid(row=1, column=0, sticky="NSEW", padx=10, pady=10)

        return_button = tk.Button(self, text="Order return", font=("Arial", 20),
                                  command=lambda: self.order_return_button())
        return_button.grid(row=1, column=1, sticky="NSEW", padx=10, pady=10)

        edit_button = tk.Button(self, text="Edit", font=("Arial", 20), command=lambda: self.edit_button())
        edit_button.grid(row=2, column=0, sticky="NSEW", padx=10, pady=10)

        report_button = tk.Button(self, text="Report", font=("Arial", 20), command=lambda: self.report_button())
        report_button.grid(row=2, column=1, sticky="NSEW", padx=10, pady=10)

    def search_and_order_button(self):
        pass

    def create_account_button(self):
        # self.pack_forget()
        # self.grid_forget()
        # frame = CreateAccount(self.master, self)
        # frame.render()
        self.controller.show_frame('CreateAccount')

    def order_return_button(self):
        pass

    def edit_button(self):
        pass

    def report_button(self):
        pass
