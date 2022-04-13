# import tkinter as tk
#
# class Example(tk.Frame):
#
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         # self.controller = controller
#         self.render()
#
#     def render(self):
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_rowconfigure(1, weight=1)
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)
#
#         tk.Label(self, text='EXAMPLE', bg='red').grid(row=0, column=0)
#
# root = tk.Tk()
# root.state('zoomed')
# app = Example(root)
# app.pack(fill="both", expand=True)
# app.mainloop()

import tkinter as tk
from tkinter import font as tkfont

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # self.state("zoomed")

        # store
        self.store = {
            "brand": "aaaa",
            "electric": False,
            "year": 1964,
            "colors": ["red", "white", "blue"]
        }

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky='nswe')

        self.show_frame("StartPage")
        # self.frames['StartPage'].tkraise()

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        # frame.tkraise()
        if hasattr(frame, 'state') and self.store == frame.state:
            frame.tkraise()
        else:
            # frame.destroy()
            # frame = eval(page_name)(parent=self.container, controller=self)
            # frame.grid(row=0, column=0, sticky='nswe')
            for widget in frame.winfo_children():
                widget.destroy()
            frame.render()
            frame.tkraise()
            frame.state = self.store

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # self.state = controller.store
        # self.render()

    def gotoPage1(self):
        print("StartPage -> PageOne", self.controller.store)
        self.controller.show_frame("PageOne")

    def gotoPage2(self):
        print("StartPage -> PageTwo", self.controller.store)
        self.controller.store['year'] = 2000
        self.controller.show_frame("PageTwo")

    def render(self):
        label = tk.Label(self, text="This is the start page "+self.controller.store['brand'], font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=self.gotoPage1)
        button2 = tk.Button(self, text="Go to Page Two",
                            command=self.gotoPage2)
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # self.state = controller.store
        # self.render()

    def gotoStartPage(self):
        thisdict = {
            "brand": "Ford",
            "electric": False,
            "year": 1964,
            "colors": ["red", "white", "blue"]
        }
        self.controller.store = thisdict
        print("PageOne -> StartPage", self.controller.store)
        self.controller.show_frame("StartPage")

    def render(self):
        label = tk.Label(self, text="This is page 1 " + str(self.controller.store['year']), font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=self.gotoStartPage)
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.state = controller.store
        # self.render()

    def render(self):
        label = tk.Label(self, text="This is page 2", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: self.controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
