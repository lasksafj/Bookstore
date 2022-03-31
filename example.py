import tkinter as tk

class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x500")
        self.res = 0;

    def showA(self):
        label1 = tk.Label(self, text="first number", fg="red")
        label1.place(x=50, y=50)
        self.entry1 = tk.Entry(self)
        self.entry1.pack()
        self.entry1.place(x=150, y=50)

    def showB(self):
        label2 = tk.Label(self, text="second number", fg="red")
        label2.place(x=50, y=100)
        self.entry2 = tk.Entry(self)
        self.entry2.pack()
        self.entry2.place(x=150, y=100)

    def showResult(self):
        res = int(self.entry1.get()) + int(self.entry2.get())
        result = tk.Label(self, text=res, fg="red")
        result.place(x=100, y=150)

    def onSumBtn(self):
        self.showResult()

    def render(self):
        self.showA()
        self.showB()
        sumBtn = tk.Button(
            self, text="sum", font=("", 12),
            command=self.onSumBtn,
        )
        sumBtn.pack()
        sumBtn.place(x=150, y=200)


if __name__ == "__main__":
    app = View()
    app.render()
    app.mainloop()
