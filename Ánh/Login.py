import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from MainMenu import MainMenu


class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Bookstore Login")
        self.master.resizable(False, False)

    def login_success(self):
        self.pack_forget()
        self.grid_forget()
        menu = MainMenu(self.master)
        menu.render()

    def input_frame(self):
        # configure the grid of the frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=2)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # widget for resizing at the corner
        ttk.Sizegrip(self).grid(row=3, column=2, sticky=tk.SE)

        # grid the frame
        self.grid(row=0, column=0)

        # fill the window with the frame
        self.pack(expand=1, fill=tk.BOTH)

        # Username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        username_entry = ttk.Entry(self, width=30)
        username_entry.grid(row=0, column=1, columnspan=5, sticky=tk.E, padx=10, pady=10)

        # Password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

        password_entry = ttk.Entry(self, show="*", width=30)
        password_entry.grid(row=1, column=1, columnspan=5, sticky=tk.E, padx=10, pady=10)

        # Login
        login_button = ttk.Button(self, text="Login", command=lambda: self.show_login(username_entry, password_entry))
        login_button.grid(row=2, column=1, columnspan=5, sticky=tk.E, padx=10, pady=10)

        # Enter bind
        self.master.bind('<Return>', lambda event: self.show_login(username_entry, password_entry))

    def show_login(self, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()

        if username == "" or password == "":
            messagebox.showinfo("", "Blank Not Allowed")

        elif username == "annieh195" and password == "190500":
            self.login_success()
        else:
            messagebox.showinfo("", "Incorrect username or password")

    def render(self):
        self.input_frame()


if __name__ == "__main__":
    app = Login()
    app.render()
    app.mainloop()
