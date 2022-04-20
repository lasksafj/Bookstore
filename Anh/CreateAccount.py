from tkinter import ttk
from tkinter import *
from tkinter import messagebox
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
        # self.phoneNumber = None
        self.render()

    def render(self):
        # configure the grid of the frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        # self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        # self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)
        # self.grid_rowconfigure(9, weight=1)
        self.grid_rowconfigure(10, weight=1)
        self.grid_rowconfigure(11, weight=1)
        # self.grid_rowconfigure(12, weight=1)
        self.grid_rowconfigure(13, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # widget for resizing at the corner
        ttk.Sizegrip(self).grid(row=13, column=2, sticky=tk.SE)

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
        num = "Phone number 123-456-7890"
        num_entry = ttk.Entry(self)
        num_entry.insert(0, num)
        num_entry.bind('<FocusIn>', lambda event: self.on_click(num_entry, num))
        num_entry.bind('<FocusOut>', lambda event: self.on_out(num_entry, num))
        num_entry.grid(row=4, columnspan=2, sticky="NSEW", padx=10, pady=10)
        self.msg_num = ttk.Label(self, text='', foreground='red')

        # Date of Birth
        dob = "Date of birth MM-DD-YYYY"
        dob_entry = ttk.Entry(self)
        dob_entry.insert(0, dob)
        dob_entry.bind('<FocusIn>', lambda event: self.on_click(dob_entry, dob))
        dob_entry.bind('<FocusOut>', lambda event: self.on_out(dob_entry, dob))
        dob_entry.grid(row=6, columnspan=2, sticky="NSEW", padx=10, pady=10)
        self.msg_dob = ttk.Label(self, text='', foreground='red')

        # Hire date
        hire = "Hire day MM-DD-YYYY"
        hire_entry = ttk.Entry(self)
        hire_entry.insert(0, hire)
        hire_entry.bind('<FocusIn>', lambda event: self.on_click(hire_entry, hire))
        hire_entry.bind('<FocusOut>', lambda event: self.on_out(hire_entry, hire))
        hire_entry.grid(row=8, columnspan=2, sticky="NSEW", padx=10, pady=10)
        self.msg_hire = ttk.Label(self, text='', foreground='red')

        # Username
        username_label = "Username"
        username_entry = ttk.Entry(self)
        username_entry.insert(0, username_label)
        username_entry.bind('<FocusIn>', lambda event: self.on_click(username_entry, username_label))
        username_entry.bind('<FocusOut>', lambda event: self.on_out(username_entry, username_label))
        username_entry.grid(row=10, columnspan=2, sticky="NSEW", padx=10, pady=10)

        # Password
        password_label = "Password"
        password_entry = ttk.Entry(self)
        password_entry.insert(0, password_label)
        password_entry.bind('<FocusIn>', lambda event: self.on_click(password_entry, password_label))
        password_entry.bind('<FocusOut>', lambda event: self.on_out(password_entry, password_label))
        password_entry.grid(row=11, columnspan=2, sticky="NSEW", padx=10, pady=10)

        # Label account
        self.msg_account = ttk.Label(self, text='', foreground='red')

        # Create
        create_button = ttk.Button(self, text="Create",
                                   command=lambda: self.insert_database(first_entry, last_entry, address_entry,
                                                                        num_entry, dob_entry, hire_entry,
                                                                        self.position_entry, username_entry,
                                                                        password_entry))
        create_button.grid(row=13, column=1, sticky="E", padx=10, pady=10)

        # Back
        back_button = ttk.Button(self, text="Back", command=self.back_button)
        back_button.grid(row=13, column=0, sticky="W", padx=10, pady=10)

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

        list_check = self.check_input(num, dob, hire, username, password)

        # insert correct format
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
        if list_check:
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
        self.controller.show_frame('MainMenu')

    def check_input(self, num, dob, hire, username, password):
        list_return = []
        wanna_insert = True
        # check phone number
        length = len(num)
        if num == "Phone number 123-456-7890":
            self.msg_num.configure(text='Phone number cannot be empty!')
            self.msg_num.grid(row=5, column=0, sticky="NSEW", padx=10, pady=10)
            wanna_insert = False
        elif length == 12 and num[3] == "-" and num[7] == "-" and num[:3].isdigit() and num[4:7].isdigit() and num[
                                                                                                               8:].isdigit():
            self.msg_num.grid_forget()
            self.msg_num.destroy()
            self.msg_num = ttk.Label(self, text='', foreground='red')
            list_return.append(num)
        else:
            self.msg_num.configure(text='Invalid Phone Number')
            self.msg_num.grid(row=5, column=0, sticky="NSEW", padx=10, pady=10)
            wanna_insert = False

        # check dob
        length = len(dob)
        if dob == "Date of birth MM-DD-YYYY":
            self.msg_dob.configure(text='Date of birth cannot be empty!')
            self.msg_dob.grid(row=7, column=0, sticky="NSEW", padx=10, pady=10)
            wanna_insert = False
        elif length == 10 and dob[2] == "-" and dob[5] == "-" and dob[:2].isdigit() and dob[3:5].isdigit() and dob[
                                                                                                               6:].isdigit():
            self.msg_dob.grid_forget()
            self.msg_dob.destroy()
            self.msg_dob = ttk.Label(self, text='', foreground='red')
            list_return.append(dob)
        else:
            self.msg_dob.configure(text='Invalid Day')
            self.msg_dob.grid(row=7, column=0, sticky="NSEW", padx=10, pady=10)
            wanna_insert = False

        # check hire day
        length = len(hire)
        if hire == "Hire day MM-DD-YYYY":
            self.msg_hire.configure(text='Hire day cannot be empty!')
            self.msg_hire.grid(row=9, column=0, sticky="NSEW", padx=10, pady=10)
            wanna_insert = False
        elif length == 10 and hire[2] == "-" and hire[5] == "-" and hire[:2].isdigit() and hire[3:5].isdigit() and hire[
                                                                                                                   6:].isdigit():
            self.msg_hire.grid_forget()
            self.msg_hire.destroy()
            self.msg_hire = ttk.Label(self, text='', foreground='red')
            list_return.append(hire)
        else:
            self.msg_hire.configure(text='Invalid Day')
            self.msg_hire.grid(row=9, column=0, sticky="NSEW", padx=10, pady=10)
            wanna_insert = False

        # check username and password
        if username == "Username" or password == "Password":
            self.msg_account.configure(text='Username and password cannot be empty!')
            self.msg_account.grid(row=12, column=0, sticky="NSEW", padx=10, pady=10)
            wanna_insert = False
        else:
            search = {
                'username': username,
                'password': password
            }
            data_check = dbsql.search_db(self.con, 'employee', search)
            if not data_check:
                self.msg_account.grid_forget()
                self.msg_account.destroy()
                self.msg_account = ttk.Label(self, text='', foreground='red')
            else:
                wanna_insert = False

        if wanna_insert == False:
            list_return = []
        return list_return