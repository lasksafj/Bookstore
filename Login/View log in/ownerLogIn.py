import tkinter as tk
from tkinter import ttk

class ownerLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bookstore")
        self.geometry("500x500")
        self.resizable(True, True)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        sg = ttk.Sizegrip(self)
        sg.grid(row=2, column=1, sticky=tk.SE)

    def create_button(self):
        create_button = tk.Button(
            self, text="Create", font=("Arial", 20),
            command=self.create_button)
        create_button.grid(row=0, column=0, sticky="NSEW", padx=10, pady=10)

    def edit_button(self):
        edit_button = tk.Button(
            self, text="Edit", font=("Arial", 20),
            command=self.edit_button)
        edit_button.grid(row=0, column=1, sticky="NSEW", padx=10, pady=10)

    def search_button(self):
        search_button = tk.Button(
            self, text="Search", font=("Arial", 20),
            command=self.search_button)
        search_button.grid(row=1, column=0, sticky="NSEW", padx=10, pady=10)

    def return_button(self):
        return_button = tk.Button(
            self, text="Return", font=("Arial", 20),
            command=self.return_button)
        return_button.grid(row=1, column=1, sticky="NSEW", padx=10, pady=10)

    def render(self):
        self.create_button()
        self.edit_button()
        self.search_button()
        self.return_button()

if __name__ == "__main__":
    app = ownerLogin()
    app.render()
    app.mainloop()