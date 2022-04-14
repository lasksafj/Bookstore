from tkinter import ttk
import tkinter as tk
import sys

sys.path.append('../')
import dbsql


class CreateAccount(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.con = dbsql.create_connection("bookstore.db")
        self.position_entry = None
        self.render()

    def render(self):
        # configure the grid of the frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # widget for resizing at the corner
        ttk.Sizegrip(self).grid(row=9, column=2, sticky=tk.SE)

        # grid the frame
        # self.grid(row=0, column=0)

        # fill the window with the frame
        # self.pack(expand=1, fill=tk.BOTH)

        page_label = ttk.Label(self, text="Create Account", font=("Arial", 30))
        page_label.grid(row=0, columnspan=2, padx=10, pady=10)

        # Position check box
        check_var1 = tk.IntVar()
        check_var2 = tk.IntVar()
        check1 = tk.Checkbutton(self, text="Assistant Manager", variable=check_var1, onvalue=1, offvalue=0, height=5,
                                width=20, command=lambda: self.clear_selection(check2, check1.cget("text")))
        check1.grid(row=1, column=0)
        check2 = tk.Checkbutton(self, text="Employee", variable=check_var2, onvalue=1, offvalue=0, height=5, width=20,
                                command=lambda: self.clear_selection(check1, check2.cget("text")))
        check2.grid(row=1, column=1)

        # First Name
        first = "First name"
        first_entry = ttk.Entry(self)
        first_entry.insert(0, first)
        first_entry.bind('<FocusIn>', lambda event: self.on_click(first_entry, first))
        first_entry.bind('<FocusOut>', lambda event: self.on_out(first_entry, first))
        first_entry.grid(row=2, column=0, sticky="NSEW", padx=10, pady=10)

        # Last Name
        last = "Last name"
        last_entry = ttk.Entry(self)
        last_entry.insert(0, last)
        last_entry.bind('<FocusIn>', lambda event: self.on_click(last_entry, last))
        last_entry.bind('<FocusOut>', lambda event: self.on_out(last_entry, last))
        last_entry.grid(row=2, column=1, sticky="NSEW", padx=10, pady=10)

        # Address
        address = "Address"
        address_entry = ttk.Entry(self)
        address_entry.insert(0, address)
        address_entry.bind('<FocusIn>', lambda event: self.on_click(address_entry, address))
        address_entry.bind('<FocusOut>', lambda event: self.on_out(address_entry, address))
        address_entry.grid(row=3, columnspan=2, sticky="NSEW", padx=10, pady=10)

        # Phone number
        num = "Phone number (123) 456-7890"
        num_entry = ttk.Entry(self)
        num_entry.insert(0, num)
        num_entry.bind('<FocusIn>', lambda event: self.on_click(num_entry, num))
        num_entry.bind('<FocusOut>', lambda event: self.on_out(num_entry, num))
        num_entry.grid(row=4, columnspan=2, sticky="NSEW", padx=10, pady=10)

        # Date of Birth
        dob = "Date of birth MM/DD/YYYY"
        dob_entry = ttk.Entry(self)
        dob_entry.insert(0, dob)
        dob_entry.bind('<FocusIn>', lambda event: self.on_click(dob_entry, dob))
        dob_entry.bind('<FocusOut>', lambda event: self.on_out(dob_entry, dob))
        dob_entry.grid(row=5, columnspan=2, sticky="NSEW", padx=10, pady=10)

        # Hire date
        hire = "Hire day MM/DD/YYYY"
        hire_entry = ttk.Entry(self)
        hire_entry.insert(0, hire)
        hire_entry.bind('<FocusIn>', lambda event: self.on_click(hire_entry, hire))
        hire_entry.bind('<FocusOut>', lambda event: self.on_out(hire_entry, hire))
        hire_entry.grid(row=6, columnspan=2, sticky="NSEW", padx=10, pady=10)

        # Username
        username_label = "Username"
        username_entry = ttk.Entry(self)
        username_entry.insert(0, username_label)
        username_entry.bind('<FocusIn>', lambda event: self.on_click(username_entry, username_label))
        username_entry.bind('<FocusOut>', lambda event: self.on_out(username_entry, username_label))
        username_entry.grid(row=7, columnspan=2, sticky="NSEW", padx=10, pady=10)

        # Password
        password_label = "Password"
        password_entry = ttk.Entry(self)
        password_entry.insert(0, password_label)
        password_entry.bind('<FocusIn>', lambda event: self.on_click(password_entry, password_label))
        password_entry.bind('<FocusOut>', lambda event: self.on_out(password_entry, password_label))
        password_entry.grid(row=8, columnspan=2, sticky="NSEW", padx=10, pady=10)

        # Create
        create_button = ttk.Button(self, text="Create",
                                   command=lambda: self.insert_database(first_entry, last_entry, address_entry,
                                                                        num_entry, dob_entry, hire_entry,
                                                                        self.position_entry, username_entry,
                                                                        password_entry))
        # create_button = ttk.Button(self, text="Create")
        create_button.grid(row=9, column=1, sticky="E", padx=10, pady=10)

        # Back
        back_button = ttk.Button(self, text="Back", command=self.back_button)
        back_button.grid(row=9, column=0, sticky="W", padx=10, pady=10)

    def insert_database(self, first_entry, last_entry, address_entry, num_entry, dob_entry, hire_entry, position_entry,
                        username_entry,
                        password_entry):

        first = first_entry.get()
        last = last_entry.get()
        address = address_entry.get()
        num = num_entry.get()
        dob = dob_entry.get()
        hire = hire_entry.get()
        position = position_entry
        username = username_entry.get()
        password = password_entry.get()

        insert = {
            'first_name': first,
            'last_name': last,
            'adress': address,
            'phone': num,
            'dob': dob,
            'hire_date': hire,
            'position': position,
            'username': username,
            'password': password
        }
        dbsql.insert_db(self.con, 'employee', insert)

    def on_click(event, input, a):
        if input.get() == a:
            input.delete(0, "end")
            input.insert(0, '')

    def on_out(event, output, a):
        if output.get() == '':
            output.insert(0, a)

    def clear_selection(self, check, text):
        check.deselect()
        self.position_entry = text

    def back_button(self):
        # self.pack_forget()
        # self.grid_forget()
        # self.previous_frame.render()
        self.controller.show_frame('MainMenu')

# if __name__ == "__main__":
#     app = CreateAccount()
#     app.render()
#     app.mainloop()
