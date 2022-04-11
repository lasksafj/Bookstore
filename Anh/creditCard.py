from tkinter import ttk
import tkinter as tk


class CreditCard(tk.Tk):
    # def __init__(self, master, previous_frame):
    #     tk.Frame.__init__(self, master)
    #     self.previous_frame = previous_frame
    #     self.master = master
    #     self.master.title("Add Card")
    #     self.master.state("zoomed")

    def __init__(self):
        super().__init__()
        self.title("Add Card")
        self.state("zoomed")

    def render(self):
        # configure the grid of the frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # widget for resizing at the corner
        # ttk.Sizegrip(self).grid(row=5, column=2, sticky="SE")

        # grid the frame
        # self.grid(row=0, column=0)

        # fill the window with the frame
        # self.pack(expand=1, fill=tk.BOTH)

        page_label = ttk.Label(self, text="Add credit or debit card", font=("Arial", 15))
        page_label.grid(row=0, columnspan=3, padx=10, pady=10)

        # Card number
        card_label = ttk.Label(self, text="Card number:")
        card_label.grid(row=1, column=0, sticky="W", padx=10, pady=10)

        card_entry = ttk.Entry(self, width=50)
        card_entry.grid(row=1, column=1, columnspan=2, sticky="NSEW", padx=10, pady=10)

        # Name on card
        name = ttk.Label(self, text="Name on card:")
        name.grid(row=2, column=0, sticky="W", padx=10, pady=10)

        name_entry = ttk.Entry(self, width=50)
        name_entry.grid(row=2, column=1, columnspan=2, sticky="NSEW", padx=10, pady=10)

        # Expiration date
        expire = ttk.Label(self, text="Expiration date:")
        expire.grid(row=3, column=0, sticky="W", padx=10, pady=10)

        expire_entry = ttk.Entry(self, width=30)
        expire_entry.grid(row=3, column=1, columnspan=2, sticky="NSEW", padx=10, pady=10)

        # Security code (sc)
        sc = ttk.Label(self, text="Security code:")
        sc.grid(row=4, column=0, sticky="W", padx=10, pady=10)

        sc_entry = ttk.Entry(self, width=30)
        sc_entry.grid(row=4, column=1, columnspan=2, sticky="NSEW", padx=10, pady=10)

        # Add card button
        add_button = ttk.Button(self, text="Add card")
        add_button.grid(row=5, column=2, sticky="E", padx=10, pady=10)

        # Back
        # back_button = ttk.Button(self, text="Back", command=self.back_button)
        back_button = ttk.Button(self, text="Back")
        back_button.grid(row=5, column=0, sticky="W", padx=10, pady=10)
    #
    # def back_button(self):
    #     self.pack_forget()
    #     self.grid_forget()
    #     self.previous_frame.render()


if __name__ == "__main__":
    app = CreditCard()
    app.render()
    app.mainloop()
