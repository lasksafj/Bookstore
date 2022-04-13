import tkinter as tk
from tkinter import font as tkfont

from Anh.MainMenu import MainMenu
from Anh.CreateAccount import CreateAccount

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.state("zoomed")

        # store
        self.store = kwargs['login_info']

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, CreateAccount):
            page_name = F.__name__
            frame = F(master=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame("MainMenu")
        # self.frames['MainMenu'].tkraise()

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        # frame.tkraise()
        if hasattr(frame, 'state') and self.store == frame.state:
            frame.tkraise()
        else:
            # self.frames[page_name].destroy()
            # self.frames[page_name] = eval(page_name)(parent=self.container, controller=self)
            # self.frames[page_name].grid(row=0, column=0, sticky='nswe')
            for widget in frame.winfo_children():
                widget.destroy()
            frame.render()
            frame.tkraise()
            frame.state = self.store


# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()
