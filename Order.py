from tkinter import *
import tkinter as tk

class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.state("zoomed")
        self.render()

    def onSumBtn(self):
        a = int(self.entry1.get())
        b = int(self.entry2.get())
        c = a + b
        self.label3.config(text=c)

    def render(self):
        for i in range(4):
            self.columnconfigure(i, weight=1)
        for i in range(3):
            self.rowconfigure(i, weight=1)

        label1 = tk.Label(self, text="number 1", fg="red")
        label1.grid(row=0, column=1)
        label2 = tk.Label(self, text="number 2", fg="red")
        label2.grid(row=1, column=1)

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0, column=2)
        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1, column=2)

        button1 = tk.Button(self, text="click me", command=self.onSumBtn)
        button1.grid(row=2, column=1)

        self.label3 = tk.Label(self, text='')
        self.label3.grid(row=2, column=2)


if __name__ == "__main__":
    app = View()
    app.mainloop()
