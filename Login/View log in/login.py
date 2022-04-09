import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bookstore")
        self.geometry("300x150")
        self.resizable(False, False)
        # self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1)

    def input_frame(self):
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
        login_button = ttk.Button(self, text="Login", command=lambda: self.showLogin(username_entry, password_entry))
        login_button.grid(row=2, column=1, columnspan=5, sticky=tk.E, padx=10, pady=10)

    def showLogin(self, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()

        if username == "" or password == "":
            messagebox.showinfo("", "Blank Not Allowed")

        elif username == "annieh195" and password == "190500":
            messagebox.showinfo("", "Login Success")

        else:
            messagebox.showinfo("", "Incorrect username or password")

    def render(self):
        self.input_frame()

if __name__ == "__main__":
    app = login()
    app.render()
    app.mainloop()