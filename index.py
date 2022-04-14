import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from app import SampleApp
import dbsql

class Start(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bookstore Login")
        self.resizable(False, False)
        self.con = dbsql.create_connection("bookstore.db")
        self.render()

    def login_success(self, data_check):
        self.destroy()
        app = SampleApp(login_info=data_check)

    def input_frame(self):
        # configure the grid of the frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=2)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # widget for resizing at the corner
        ttk.Sizegrip(self).grid(row=3, column=2, sticky=tk.SE)

        # Username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(row=0, column=0, padx=10, pady=10)

        username_entry = ttk.Entry(self, width=30)
        username_entry.grid(row=0, column=1, columnspan=5, padx=10, pady=10)

        # Password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(row=1, column=0, padx=10, pady=10)

        password_entry = ttk.Entry(self, show="*", width=30)
        password_entry.grid(row=1, column=1, columnspan=5, padx=10, pady=10)

        # Login
        login_button = ttk.Button(self, text="Login", command=lambda: self.show_login(username_entry, password_entry))
        login_button.grid(row=2, column=1, columnspan=5, padx=10, pady=10)

        # Enter bind
        self.bind('<Return>', lambda event: self.show_login(username_entry, password_entry))

    def show_login(self, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()
        if username == "" or password == "":
            messagebox.showinfo("", "Blank Not Allowed")
        else:
            search = {
                'username': username,
                'password': password
            }
            data_check = dbsql.search_db(self.con, 'employee', search)
            if not data_check:
                messagebox.showinfo("", "Incorrect username or password")
            else:
                self.login_success(data_check[0])

    def render(self):
        self.input_frame()

if __name__ == "__main__":
    app = Start()
    app.mainloop()
