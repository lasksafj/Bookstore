# import tkinter as tk
#
# class View(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Calculator")
#         # width= self.winfo_screenwidth()
#         # height= self.winfo_screenheight()
#         # self.geometry("%dx%d" % (width, height))
#         # self.geometry("400x500")
#         self.state('zoomed')
#         self.res = 0;
#
#     def showA(self):
#         label1 = tk.Label(self, text="first number", fg="red")
#         label1.place(x=50, y=50)
#         self.entry1 = tk.Entry(self)
#         self.entry1.pack()
#         self.entry1.place(x=150, y=50)
#
#     def showB(self):
#         label2 = tk.Label(self, text="second number", fg="red")
#         label2.place(x=50, y=100)
#         self.entry2 = tk.Entry(self)
#         self.entry2.pack()
#         self.entry2.place(x=150, y=100)
#
#     def showResult(self):
#         res = int(self.entry1.get()) + int(self.entry2.get())
#         result = tk.Label(self, text=res, fg="red")
#         result.place(x=100, y=150)
#
#     def onSumBtn(self):
#         self.showResult()
#
#     def render(self):
#         # self.showA()
#         # self.showB()
#         # sumBtn = tk.Button(
#         #     self, text="sum", font=("", 12),
#         #     command=self.onSumBtn,
#         # )
#         # sumBtn.pack()
#         # sumBtn.place(x=150, y=200)
#
#         for i in range(4):
#             self.columnconfigure(i, weight=1)
#         for i in range(4):
#             self.rowconfigure(i, weight=1)
#
#         label1 = tk.Label(self, text='first number', fg='red')
#         label1.config(bg='blue')
#         label1.grid(row=0, column=0)
#         entry1 = tk.Entry(self).grid(row=0, column=2, sticky='swne')
#
#         tk.Label(self, text='second number', fg='red').grid(row=1, column=0, columnspan=2)
#         entry2 = tk.Entry(self).grid(row=1, column=2)
#
#
# if __name__ == "__main__":
#     app = View()
#     app.render()
#     app.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
#
# class View(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Calculator")
#         self.state("zoomed")
#         self.render()
#
#     def onSumBtn(self):
#         a = int(self.entry1.get())
#         b = int(self.entry2.get())
#         c = a + b
#         self.label3.config(text=c)
#
#     def render(self):
#         for i in range(4):
#             self.columnconfigure(i, weight=1)
#         for i in range(3):
#             self.rowconfigure(i, weight=1)
#
#         label1 = tk.Label(self, text="number 1", fg="red")
#         label1.grid(row=0, column=1)
#         label2 = tk.Label(self, text="number 2", fg="red")
#         label2.grid(row=1, column=1)
#
#         self.entry1 = tk.Entry(self)
#         self.entry1.grid(row=0, column=2)
#         self.entry2 = tk.Entry(self)
#         self.entry2.grid(row=1, column=2)
#
#         button1 = tk.Button(self, text="click me", command=self.onSumBtn)
#         button1.grid(row=2, column=1)
#
#         self.label3 = tk.Label(self, text='')
#         self.label3.grid(row=2, column=2)
#
#         self.image1 = ImageTk.PhotoImage(Image.open('logo.png'))
#         tk.Label(self, image=self.image1).grid(row=0, column=0)
#
#
# if __name__ == "__main__":
#     app = View()
#     app.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Treeview demo')
        self.geometry('620x200')

        self.tree = self.create_tree_widget()

    def create_tree_widget(self):
        columns = ('first_name', 'last_name', 'email')
        tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        tree.heading('first_name', text='First Name')
        tree.heading('last_name', text='Last Name')
        tree.heading('email', text='Email')

        tree.bind('<<TreeviewSelect>>', self.item_selected)
        tree.grid(row=0, column=0, sticky=tk.NSEW)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # generate sample data
        contacts = []
        for n in range(1, 100):
            contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview
        for contact in contacts:
            tree.insert('', tk.END, values=contact)

        return tree

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))


if __name__ == '__main__':
    app = App()
    app.mainloop()
