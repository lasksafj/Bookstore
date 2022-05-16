from cgitb import text
from tkinter import *
import tkinter as tk
from tkinter import ttk
import collections

class List(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BOOKSTORE")
        self.geometry("400x500")
        self.state('zoomed')
        #Create Label
        list_label = tk.Label(self, text="Book List", font=("Helvatica", 30))
        list_label.pack(pady=20)
        #Add Data
        self.data = [
            ['AUST1234', 'Poor Dad Rich Dad', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold', '....'],
            ['AUST1234', 'Harry Porter', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','....'],
            ['AUST1234', 'Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','....'],
            ['AUST1234', 'Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','....'],
            ['AUST1235', 'Love', 'Jane Austen (101)', 'N/A', '1812', '1', '3000', '5900', 'Good', 'Sold','....'],
            ['AUST1234', 'Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','....'],
            ['AUST0234', 'Dragon Balls', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','....'],
            ['AUST1834', 'Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','....'],
            ['AUST1234', 'Dragon Balls', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','....']
        ]
        # print(type(self.data))
        self.count = 0
        self.index=0
        
    

    def data_hadle(self):
        self.current_data = list()
        for row in self.data:
            temp = tuple()
            for x in [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]]:
                temp += (x, )
            self.current_data.append(temp)

        # print(self.current_data)
        val = collections.Counter(self.current_data)
        self.book_list = list()
        self.duplicate = [*val.keys()]
        # for x in range(len(self.duplicate)):
        #     self.book_list[x] += (*val.values()[x])
        for i in self.duplicate:
            self.book_list.append(i + (val[i],))
        # print(self.book_list)
        return self.book_list


    def doubleClick(self, event):
        self.window = Toplevel()
        self.window.geometry("500x600")
        self.window.title('Book Details')
        x = self.list_tree.item(int(self.list_tree.selection()[0]), 'value')


        title_label = Label(self.window, text=x[0], font=("Helvatica", 20))
        title_label.pack(pady=20)
        
        author_label = Label(self.window, text='Author: {}'.format(x[1]))
        description_label = Label(self.window, text='.............................................................................')

        author_label.pack(pady=10, padx=10,anchor=W)
        description_label.pack(pady=10, padx=10, anchor=W)

        close = Button(self.window, text='Close Tab', command=self.window.destroy)
        close.pack(pady=10)




    def list_book(self, book_list):

        #Create List Frame
        self.frame1 = LabelFrame(self, text="Book List....", padx=10, pady=10)
        self.frame1.pack(padx=10, pady=10)


        # self.style = ttk.Style()
        # self.style.configure("Treeview", 
        #     backgoround='silver',
        #     foreground='black',
        #     rowheight=25,
        #     fieldbackground='silver'       
        #     )
        # self.style.map('Treeview',
        #         bakcground=[('selected', 'green')])

        #create tree view
        self.list_scroll = ttk.Scrollbar(self.frame1)
        self.list_scroll.pack(side=RIGHT, fill=Y)
        self.list_tree = ttk.Treeview(self.frame1)
        # self.list_tree.configure('Treeview', rowheight=40)

        self.list_tree['columns'] = ('Title', 'Author', 'Publisher', 'Year', 'Edition', 'Cost', 'Retail', 'Condition', 'Status', 'Available')
        
        #Formate Columns
        self.list_tree.column('#0', width=0, stretch=NO)
        # self.list_tree.column('Book ID',anchor=CENTER, width=100)
        self.list_tree.column('Title',anchor=CENTER, width=400)
        self.list_tree.column('Author',anchor=CENTER, width=200)
        self.list_tree.column('Publisher',anchor=CENTER, width=150)
        self.list_tree.column('Year',anchor=CENTER, width=80)
        self.list_tree.column('Edition',anchor=CENTER, width=100)
        self.list_tree.column('Cost',anchor=CENTER, width=100)
        self.list_tree.column('Retail',anchor=CENTER, width=100)
        self.list_tree.column('Condition',anchor=CENTER, width=100)
        self.list_tree.column('Status',anchor=CENTER, width=100)
        self.list_tree.column('Available',anchor=CENTER, width=80)

        #Create Heading
        self.list_tree.heading('#0', text="", anchor=CENTER)
        # self.list_tree.heading('Book ID', text="BookID", anchor=CENTER)
        self.list_tree.heading('Title', text="Title", anchor=CENTER)
        self.list_tree.heading('Author', text="Author", anchor=CENTER)
        self.list_tree.heading('Publisher', text="Publisher", anchor=CENTER)
        self.list_tree.heading('Year', text="Year", anchor=CENTER)
        self.list_tree.heading('Edition', text="Edition", anchor=CENTER)
        self.list_tree.heading('Cost', text="Cost", anchor=CENTER)
        self.list_tree.heading('Retail', text="Retail", anchor=CENTER)
        self.list_tree.heading('Condition', text="Condition", anchor=CENTER)
        self.list_tree.heading('Status', text="Status", anchor=CENTER)
        self.list_tree.heading('Available', text="Available", anchor=CENTER)

        

       
        
        for record in self.book_list:
            self.list_tree.insert(parent='', index='end', iid=self.count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]))
            self.count+=1
        ''''
        self.list_tree.insert(parent='', index='end', iid=0, text='', values=('AUST1234', 'Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','...'))
        self.list_tree.insert(parent='', index='end', iid=1, text='', values=('AUST1234', 'Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold', '....'))
        self.list_tree.insert(parent='', index='end', iid=2, text='', values=('AUST1234', 'Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold', '....'))
        '''
        self.list_tree.pack(pady=20)

        #create mouse click
        self.list_tree.bind('<Double-1>', self.doubleClick)
        self.list_tree.bind('<Button-3>', self.get_click)
        self.list_tree.bind('<Return>', self.get_click)
        # self.list_tree.bind('<Button-1>', self.)
        
    
    def get_click(self, event):
        selects = self.list_tree.focus()
        print(selects)
        for select in selects:
            x = self.list_tree.item(int(select), 'value')
            self.cart_tree.insert(parent='', index='end', iid=self.index, text='', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]))
            self.index+=1

        # for x in selects:
        #     self.list_tree.delete(x)

    def pick(self):
        selects = self.list_tree.selection()
        for select in selects:
            x = self.list_tree.item(int(select), 'value')
            # print(x)
            self.cart_tree.insert(parent='', index='end', iid=self.index, text='', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]))
            self.index+=1

        # for x in selects:
        #     self.list_tree.delete(x)

    def remove(self):
        selects = self.cart_tree.selection()
        for select in selects:
            x = self.cart_tree.item(int(select), 'value')
            self.list_tree.insert(parent='', index='end', iid=self.count, text='', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]))
            self.count+=1

        for x in selects:
            self.cart_tree.delete(x)

    def remove_click(self, event):
        selects = self.cart_tree.selection()
        for select in selects:
            x = self.cart_tree.item(int(select), 'value')
            self.list_tree.insert(parent='', index='end', iid=self.count, text='', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]))
            self.count+=1

        for x in selects:
            self.cart_tree.delete(x)

    def button_book(self):
        self.frame2 = LabelFrame(self, text="Buttons...", padx=10, pady=10)
        self.frame2.pack(padx=10, pady=10)

        self.back = Button(self.frame2, text="<<")
        self.back.grid(row=0, column=0, padx=100, sticky=W)

        self.get_box = Entry(self.frame2)
        self.get_box.grid(row=0, column=1, pady=10)

        self.pick = Button(self.frame2, text='Pick', padx=100, command=self.pick)
        self.pick.grid(row=0, column=3, pady=10, padx=100)

        self.remove = Button(self.frame2, text='Remove', padx=100, command=self.remove)
        self.remove.grid(row=0, column=4, pady=10, padx=100)


        self.order = Button(self.frame2, text='Create Order', padx=300)
        self.order.grid(row=1, column=1, columnspan=4,pady=10)

    def cart_book(self):
        self.frame3 = LabelFrame(self, text="Shopping Cart...", padx=10, pady=10)
        self.frame3.pack(padx=10, pady=10)

        self.cart_tree = ttk.Treeview(self.frame3)
        self.cart_tree['columns'] = ('Title', 'Author', 'Publisher', 'Year', 'Edition', 'Cost', 'Retail', 'Condition', 'Status', 'Pick')
        
        #Formate Columns
        self.cart_tree.column('#0', width=0, stretch=NO)
        # self.cart_tree.column('Book ID',anchor=CENTER, width=100)
        self.cart_tree.column('Title',anchor=CENTER, width=400)
        self.cart_tree.column('Author',anchor=CENTER, width=200)
        self.cart_tree.column('Publisher',anchor=CENTER, width=150)
        self.cart_tree.column('Year',anchor=CENTER, width=80)
        self.cart_tree.column('Edition',anchor=CENTER, width=100)
        self.cart_tree.column('Cost',anchor=CENTER, width=100)
        self.cart_tree.column('Retail',anchor=CENTER, width=100)
        self.cart_tree.column('Condition',anchor=CENTER, width=100)
        self.cart_tree.column('Status',anchor=CENTER, width=100)
        self.cart_tree.column('Pick',anchor=CENTER, width=80)

        #Create Heading
        self.cart_tree.heading('#0', text="", anchor=CENTER)
        # self.cart_tree.heading('Book ID', text="BookID", anchor=CENTER)
        self.cart_tree.heading('Title', text="Title", anchor=CENTER)
        self.cart_tree.heading('Author', text="Author", anchor=CENTER)
        self.cart_tree.heading('Publisher', text="Publisher", anchor=CENTER)
        self.cart_tree.heading('Year', text="Year", anchor=CENTER)
        self.cart_tree.heading('Edition', text="Edition", anchor=CENTER)
        self.cart_tree.heading('Cost', text="Cost", anchor=CENTER)
        self.cart_tree.heading('Retail', text="Retail", anchor=CENTER)
        self.cart_tree.heading('Condition', text="Condition", anchor=CENTER)
        self.cart_tree.heading('Status', text="Status", anchor=CENTER)
        self.cart_tree.heading('Pick', text='Pick', anchor=CENTER)

        

        self.cart_tree.pack(pady=20)
        self.cart_tree.bind('<Double-1>', self.doubleClick)
        self.cart_tree.bind('<Button-3>', self.remove_click)
        self.cart_tree.bind('<Return>', self.remove_click)



if __name__ == "__main__":
    app = List()
    app.list_book(app.data_hadle())
    app.button_book()
    
    app.cart_book()
    app.mainloop()