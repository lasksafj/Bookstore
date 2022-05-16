from textwrap import fill
import tkinter as tk
from tkinter import ttk
from turtle import width
import collections
from unicodedata import numeric


class Example(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # self.controller = controller
        # self.temp_list = list()
        self.temp_list2 = list()
        self.cart_count = 0

    def render(self):
        '''Create the grid of window with 20rows and 25 columns'''
        for i in range(20):
            self.grid_rowconfigure(i, weight=1)
        for i in range(25):
            self.grid_columnconfigure(i, weight=1)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        font_size = screen_width/20

        store_label = tk.Label(self, text="Book List", font= font_size, bg='red')
        store_label.grid(row=1, column=0, sticky='nsew', rowspan=2, columnspan=25)

        
        self.count = 0
        self.index=0
        self.data = self.handle_data()
        self.style_tree()
        self.list_book(self.data)
        self.button_book()
        self.cart_book()
        
        
    def doubleClick1(self, event):
        self.window = tk.Toplevel()
        self.window.geometry("500x600")
        self.window.title('Book Details')
        x = self.list_tree.item(int(self.list_tree.selection()[0]), 'value')


        title_label = tk.Label(self.window, text=x[0], font=("Helvatica", 20))
        title_label.pack(pady=20)
        
        author_label = tk.Label(self.window, text='Author: {}'.format(x[1]))
        description_label = tk.Label(self.window, text='.............................................................................')

        author_label.pack(pady=10, padx=10,anchor=tk.W)
        description_label.pack(pady=10, padx=10, anchor=tk.W)

        close = tk.Button(self.window, text='Close Tab', command=self.window.destroy)
        close.pack(pady=10)

    def doubleClick2(self, event):
        self.window = tk.Toplevel()
        self.window.geometry("500x600")
        self.window.title('Book Details')
        x = self.cart_tree.item(int(self.cart_tree.selection()[0]), 'value')


        title_label = tk.Label(self.window, text=x[0], font=("Helvatica", 20))
        title_label.pack(pady=20)
        
        author_label = tk.Label(self.window, text='Author: {}'.format(x[1]))
        description_label = tk.Label(self.window, text='.............................................................................')

        author_label.pack(pady=10, padx=10,anchor=tk.W)
        description_label.pack(pady=10, padx=10, anchor=tk.W)

        close = tk.Button(self.window, text='Close Tab', command=self.window.destroy)
        close.pack(pady=10)

    def style_tree(self):
        self.style = ttk.Style()

        self.style.theme_use('default')

        self.style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=20,
                fielbackground="#D3D3D3"
        
        )

        self.style.map('Treeview',
                background=[('selected', '#347083')]
        )

    def handle_data(self):
        data = [
            ('AUST1234', 'Poor Dad Rich Dad', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold', '....'),
            ('AUST1234', 'Harry Porter', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','....'),
            ('AUST1234', 'Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','....'),
            ('AUST1234', 'Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','....'),
            ('AUST1235', 'Love', 'Jane Austen (101)', 'N/A', '1812', '1', '3000', '5900', 'Good', 'Sold','....'),
            ('AUST1234', 'Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','....'),
            ('AUST0234', 'Dragon Balls', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','....'),
            ('AUST1834', 'Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','....'),
            ('AUST1234', 'Dragon Balls', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold','....')
        ]

        self.current_data = list()
        for row in data:
            temp = tuple()
            for x in [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]]:
                temp += (x, )
            self.current_data.append(temp)
            self.modify_data(self.current_data)

    def modify_data(self, original_data):
        val = collections.Counter(original_data)
        self.book_list = list()
        self.duplicate = [*val.keys()]
        for i in self.duplicate:
            self.book_list.append(i + (val[i],))
        return self.book_list


    def pick_book(self):
        '''Show books in the Listbook frame'''
        self.notice_label.config(text="")
        temp_list = list()
        # try:
        int(self.get_box.get())
        selects = self.list_tree.focus()
        x = self.list_tree.item(selects, 'value')
        y = list(x)
        z = y.pop(9)
        h = tuple(y)
        print(h)
        if int(self.get_box.get()) > int(x[9]) or int(self.get_box.get()) < 1: 
            self.notice_label.config(text='Out of Range')
        else:
            temp = list()
            num_cart = self.cart_tree.get_children()
            for i in num_cart:
                temp.append(self.cart_tree.item(i, 'value'))
            # print(temp)
            # for item in self.cart_tree.get_children():
            #     self.cart_tree.delete(item)
            for i in temp:
                y = list(i)
                z = y.pop(9)
                temp_list.append(tuple(y))
            print(temp_list)
            # print(self.temp_list)
            # curent_list = self.modify_data(self.temp_list)
            # for record in curent_list:
            temp_index = h in temp_list
            # print(temp)
            print(temp_index)
            if temp_index == False:
                if self.index % 2 == 0:
                    self.cart_tree.insert(parent='', index='end', iid=self.index, text='', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], self.get_box.get()), tags='evenrow')
                else:
                    self.cart_tree.insert(parent='', index='end', iid=self.index, text='', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], self.get_box.get()), tags='oddrow')
                self.index+=1
            else:
                index_cart = temp_list.index(h)
                print(index_cart)
                a = self.cart_tree.item(int(index_cart), 'value')
                
                print(a)
                self.cart_tree.item(int(index_cart), text="", values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], int(a[9]) + int(self.get_box.get())))
            self.list_tree.item(int(selects), text="", values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], int(x[9]) - int(self.get_box.get())))
            self.get_box.delete(0, tk.END)
            self.get_box.insert(0, 1)

        # except ValueError:
        #     self.notice_label.config(text='This is NOT a number. Please, enter numbers!')

    def remove_book(self):
        self.notice_label.config(text="")
        num_list = self.list_tree.get_children()
        temp = list()
        for i in num_list:
            temp.append(self.list_tree.item(i, 'value'))
        print(temp)
        try:
            int(self.get_box.get())
            selects = self.cart_tree.focus()
            x = self.cart_tree.item(selects, 'value')
            # print(x)
            y = list(x)
            # print(y)
            z = y.pop(9)
            h = tuple(y)
            # print(h)
            if int(self.remove_box.get()) > int(x[9]) or int(self.remove_box.get()) < 1:
                self.notice_label.config(text='Out of Range')
            else:
                temp.append(x)
                for i in temp:
                    y = list(i)
                    z = y.pop(9)
                    self.temp_list2.append(tuple(y))
                # print(self.temp_list2)
            temp_index = self.temp_list2.index(h)
            # print(temp_index)
            self.list_tree.item(temp_index, text="", values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], int(temp[temp_index][9]) + int(self.remove_box.get())))
            self.cart_tree.item(int(selects), text="", values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], int(x[9]) - int(self.remove_box.get())))
            if int(x[9]) == 1:
                self.cart_tree.delete(selects)
        except ValueError:
            self.notice_label.config(text='This is NOT a number. Please, enter numbers!')
        self.get_box.delete(0, tk.END)
        self.get_box.insert(0, 1)
        # self.temp_list.clear()
        
    def clear_all(self):
        num_list = self.list_tree.get_children()
        num_cart = self.cart_tree.get_children()
        draft_list = list()
        draft_cart = list()
        num_list1 = list()
        num_list2 = list()
        for i in num_list:
            num_list1.append(list(self.list_tree.item(i, 'value')))
            draft_list.append(tuple(list(self.list_tree.item(i, 'value')[0:9])))
        # print(draft_list)
        for i in num_cart:
            num_list2.append(list(self.cart_tree.item(i, 'value'))[9])
            # print(num_list)
            draft_cart.append(tuple(list(self.cart_tree.item(i, 'value')[0:9])))
        # print(draft_cart)
        x = 0
        for i in draft_cart:
            index_cart = draft_list.index(i)
            self.list_tree.item(index_cart, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], int(num_list1[index_cart][9]) + int(num_list2[x])))
            x+=1

        for item in self.cart_tree.get_children():
            self.cart_tree.delete(item)
        # self.temp_list.clear()


    def list_book(self, book_list):
        #Create List Frame
        self.frame1 = tk.LabelFrame(self, text="Book List....", padx=20, pady=5)
        self.frame1.grid(row=5, column=1, columnspan=22)
        frame_width = self.frame1.winfo_screenwidth() * 23/25
        # print(frame_width)
        width_col = frame_width/11

        self.list_scroll = ttk.Scrollbar(self.frame1)
        self.list_scroll.grid(row=0, column=1, sticky=tk.NS)
        self.list_tree = ttk.Treeview(self.frame1, yscrollcommand=self.list_scroll.set, selectmode="extended")
        self.list_tree.grid(row=0, column=0)

        self.list_scroll.config(command=self.list_tree.yview)

        self.list_tree['columns'] = ('Title', 'Author', 'Publisher', 'Year', 'Edition', 'Cost', 'Retail', 'Condition', 'Status', 'Available')
        #Formate Columns
        self.list_tree.column('#0', width=0, stretch=tk.NO)
        # self.list_tree.column('Book ID',anchor=CENTER, width=100)
        self.list_tree.column('Title',anchor=tk.CENTER, width=int(width_col*2))
        self.list_tree.column('Author',anchor=tk.CENTER, width=int(width_col))
        self.list_tree.column('Publisher',anchor=tk.CENTER, width=int(width_col))
        self.list_tree.column('Year',anchor=tk.CENTER, width=int(width_col))
        self.list_tree.column('Edition',anchor=tk.CENTER, width=int(width_col))
        self.list_tree.column('Cost',anchor=tk.CENTER, width=int(width_col))
        self.list_tree.column('Retail',anchor=tk.CENTER, width=int(width_col))
        self.list_tree.column('Condition',anchor=tk.CENTER, width=int(width_col))
        self.list_tree.column('Status',anchor=tk.CENTER, width=int(width_col))
        self.list_tree.column('Available',anchor=tk.CENTER, width=int(width_col))

        #Create Heading
        self.list_tree.heading('#0', text="", anchor=tk.CENTER)
        # self.list_tree.heading('Book ID', text="BookID", anchor=CENTER)
        self.list_tree.heading('Title', text="Title", anchor=tk.CENTER)
        self.list_tree.heading('Author', text="Author", anchor=tk.CENTER)
        self.list_tree.heading('Publisher', text="Publisher", anchor=tk.CENTER)
        self.list_tree.heading('Year', text="Year", anchor=tk.CENTER)
        self.list_tree.heading('Edition', text="Edition", anchor=tk.CENTER)
        self.list_tree.heading('Cost', text="Cost", anchor=tk.CENTER)
        self.list_tree.heading('Retail', text="Retail", anchor=tk.CENTER)
        self.list_tree.heading('Condition', text="Condition", anchor=tk.CENTER)
        self.list_tree.heading('Status', text="Status", anchor=tk.CENTER)
        self.list_tree.heading('Available', text="Available", anchor=tk.CENTER)

        self.list_tree.tag_configure('oddrow', background='white')
        self.list_tree.tag_configure('evenrow', background='lightblue')

        # print(self.book_list)
        for record in self.book_list:
            if self.count % 2 == 0:
                self.list_tree.insert(parent='', index='end', iid=self.count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags='evenrow')
            else:
                self.list_tree.insert(parent='', index='end', iid=self.count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags='oddrow')
            self.count+=1

        self.list_tree.bind('<Double-1>', self.doubleClick1)
        

    def button_book(self):
        self.frame2 = tk.LabelFrame(self, text="Buttons...", padx=10, pady=5)
        self.frame2.grid(row=8, column=1, columnspan=22)

        self.backBtn = tk.Button(self.frame2, text="<<", pady=20)
        self.backBtn.grid(row=0, column=0, rowspan=4, padx= 50, sticky=tk.W)

        self.search_button = tk.Button(self.frame2, text='Search', padx=50)
        self.search_button.grid(row=0, column=1, columnspan=4)

        self.get_box = tk.Entry(self.frame2)
        self.get_box.insert(0, 1)
        self.get_box.grid(row=1, column=1, pady=10, sticky=tk.W)

        self.get_button =tk.Button(self.frame2, text='Pick', command=self.pick_book)
        self.get_button.grid(row=1, column=2, pady=1)

        self.notice_label = tk.Label(self.frame2, text='')
        self.notice_label.grid(row=2, column=1,pady=10, columnspan=4)

        self.entry = tk.Label(self.frame2, text='')
        self.entry.grid(row=1, column=3, padx=20)

        self.remove_box =tk.Entry(self.frame2)
        self.remove_box.insert(0, 1)
        self.remove_box.grid(row=1, column=4, pady=10)

        self.remove_button = tk.Button(self.frame2, text='Remove', command=self.remove_book)
        self.remove_button.grid(row=1, column=5, pady=10)

        self.clear_all = tk.Button(self.frame2, text='Clear All', command=self.clear_all)
        self.clear_all.grid(row=1, column=6, padx=40, pady=10)

        self.order_button = tk.Button(self.frame2, text='Create Order', padx=50)
        self.order_button.grid(row=3, column=1, columnspan=4)

        

    def cart_book(self):

        #Create List Frame
        self.frame3 = tk.LabelFrame(self, text="Shopping Cart....", padx=20, pady=5)
        self.frame3.grid(row=12, column=1, columnspan=22)
        frame_width = self.frame1.winfo_screenwidth() * 23/25
        width_col = frame_width/11

        self.cart_scroll = ttk.Scrollbar(self.frame3)
        self.cart_scroll.grid(row=0, column=1, sticky=tk.NS)
        self.cart_tree = ttk.Treeview(self.frame3, yscrollcommand=self.cart_scroll.set, selectmode="extended")
        self.cart_tree.grid(row=0, column=0)

        self.cart_scroll.config(command=self.cart_tree.yview)


        self.cart_tree['columns'] = ('Title', 'Author', 'Publisher', 'Year', 'Edition', 'Cost', 'Retail', 'Condition', 'Status', 'Available')
        #Formate Columns
        self.cart_tree.column('#0', width=0, stretch=tk.NO)
        # self.list_tree.column('Book ID',anchor=CENTER, width=100)
        self.cart_tree.column('Title',anchor=tk.CENTER, width=int(width_col*2))
        self.cart_tree.column('Author',anchor=tk.CENTER, width=int(width_col))
        self.cart_tree.column('Publisher',anchor=tk.CENTER, width=int(width_col))
        self.cart_tree.column('Year',anchor=tk.CENTER, width=int(width_col))
        self.cart_tree.column('Edition',anchor=tk.CENTER, width=int(width_col))
        self.cart_tree.column('Cost',anchor=tk.CENTER, width=int(width_col))
        self.cart_tree.column('Retail',anchor=tk.CENTER, width=int(width_col))
        self.cart_tree.column('Condition',anchor=tk.CENTER, width=int(width_col))
        self.cart_tree.column('Status',anchor=tk.CENTER, width=int(width_col))
        self.cart_tree.column('Available',anchor=tk.CENTER, width=int(width_col))

        #Create Heading
        self.cart_tree.heading('#0', text="", anchor=tk.CENTER)
        # self.list_tree.heading('Book ID', text="BookID", anchor=CENTER)
        self.cart_tree.heading('Title', text="Title", anchor=tk.CENTER)
        self.cart_tree.heading('Author', text="Author", anchor=tk.CENTER)
        self.cart_tree.heading('Publisher', text="Publisher", anchor=tk.CENTER)
        self.cart_tree.heading('Year', text="Year", anchor=tk.CENTER)
        self.cart_tree.heading('Edition', text="Edition", anchor=tk.CENTER)
        self.cart_tree.heading('Cost', text="Cost", anchor=tk.CENTER)
        self.cart_tree.heading('Retail', text="Retail", anchor=tk.CENTER)
        self.cart_tree.heading('Condition', text="Condition", anchor=tk.CENTER)
        self.cart_tree.heading('Status', text="Status", anchor=tk.CENTER)
        self.cart_tree.heading('Available', text="Available", anchor=tk.CENTER)

        self.cart_tree.tag_configure('oddrow', background='white')
        self.cart_tree.tag_configure('evenrow', background='lightblue')

        self.cart_tree.bind('<Double-1>', self.doubleClick2)

       






root = tk.Tk()
root.state('zoomed')
app = Example(root)
app.render()
app.pack(fill="both", expand=True)


app.mainloop()