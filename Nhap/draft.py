
import tkinter as tk
from tkinter import ttk
from turtle import width
import collections


class OrderDetail(tk.Frame):

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        # self.render()
        
    def render(self):
        '''Create the grid of window with 20rows and 25 columns'''
        for i in range(20):
            self.grid_rowconfigure(i, weight=1)
        for i in range(25):
            self.grid_columnconfigure(i, weight=1)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.font_size = screen_width/20

        store_label = tk.Label(self, text="Order Detail", font= (self.font_size, 25))
        store_label.grid(row=0, column=0, sticky='nsew', rowspan=2, columnspan=25)

        chosen_book = tk.Label(self, text="Chosen Books", font=(self.font_size, 15, 'underline'))
        chosen_book.grid(row=2, column=1)

        search = {
            'status': 'Available'
        }
        data = self.controller.db.search_db(self.controller.con, 'books', search)
        print('data', data)
        final_list = self.get_iD(self.handle_data(self.controller.store['cart_tree']), data)
        print('final', final_list)
        self.shopping_cart(final_list)
    

    def handle_data(self, book_list):
        print('booooooook', book_list)
        current_list = list()
        for i in book_list:
            x = list(i)
            y = x.pop(5)
            y = x.pop(7)
            z = x.pop(8)
            for j in range(int(z)):
                temp = list(x)
                current_list.append(temp)
        return current_list

    def remove_book(self, index, final_list):
        print(index)
        print(final_list)

    def get_iD(self, current_list, data):
        print('data.......', data)
        iD_list = list()
        print('current lisstsss', current_list)

        for i in current_list:
            for j in data:
                check = set(i).issubset(j)
                print(check)
                if check == True and j[0] not in iD_list:
                    iD_list.append(j[0])
                    break

        for i in range(len(iD_list)):
            current_list[i].insert(0, iD_list[i])
        print('current_list', current_list)
        return current_list


    def shopping_cart(self, final_list):

        window_frame = tk.LabelFrame(self, text='Shopping Cart....',pady=20, padx=5)
        window_frame.grid(row=3, column=0, columnspan=23)

        specify_font = (self.font_size, 12, 'bold', 'underline')

        iD_title = tk.Label(window_frame, text='Book ID', font=specify_font)
        iD_title.grid(row=0, column=0)

        title_label = tk.Label(window_frame, text="Title", font=specify_font)
        title_label.grid(row=0, column=1)

        author_label = tk.Label(window_frame, text="Author", font=specify_font)
        author_label.grid(row=0, column=2)

        publisher_label = tk.Label(window_frame, text="Publisher", font=specify_font)
        publisher_label.grid(row=0, column=3)

        year_label = tk.Label(window_frame, text="Year", font=specify_font)
        year_label.grid(row=0, column=4)

        edition_label = tk.Label(window_frame, text="Edition", font=specify_font)
        edition_label.grid(row=0, column=5)

        retail_label = tk.Label(window_frame, text="Retail Price", font=specify_font)
        retail_label.grid(row=0, column=6)

        condition_label = tk.Label(window_frame, text="Condition", font=specify_font)
        condition_label.grid(row=0, column=7)

        num_label = tk.Label(window_frame, text="Amount", font=specify_font)
        num_label.grid(row=0, column=8)

        # index = 1
        total_price = 0.0
        for index, i in enumerate(final_list):
            num = 0
            index += 1
            print('asdasdasd', i)
            total_price += float(i[6])
            for x in i:
                order_label = tk.Label(window_frame, text=x)
                order_label.grid(row=index, column=num, padx=50, pady=10)
                num +=1
            remove_button = tk.Button(window_frame, text="Remove", command=lambda: self.remove_book(index, final_list))
            remove_button.grid(row=index, column=num)
            # index +=1
    
        total_label = tk.Label(self, text="Total Price: ", font=(self.font_size, 15, 'underline'))
        total_label.grid(row=4, column=18)

        price_label = tk.Label(self, text="{:.2f}$".format(total_price), font=(self.font_size, 15))
        price_label.grid(row=4, column=19, sticky=tk.W)

        continue_button = tk.Button(self, text="Payment", padx=70)
        continue_button.grid(row=5, column=18, columnspan=2)

        back_button = tk.Button(self, text='<<', padx=20)
        back_button.grid(row=5, column=1)





    
# data = [
#             ('AUST1234', 'Poor Dad Rich Dad', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Available', 'Fiction','....'),
#             ('AUST1235', 'Harry Porter', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold', 'Fiction','....'),
#             ('AUST1236', 'Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Available', 'Fiction', '....'),
#             ('AUST1237', 'Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold', 'Fiction','....'),
#             ('AUST1238', 'Love', 'Jane Austen (101)', 'N/A', '1812', '1', '3000', '5900', 'Good', 'Sold', 'Fiction','....'),
#             ('AUST1239', 'Captain American', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Available', 'Fiction', '....'),
#             ('AUST0234', 'Dragon Balls', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Available', 'Fiction', '....'),
#             ('AUST1834', 'Iron Man', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold', 'Fiction','....'),
#             ('AUST1241', 'Dragon Balls', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Available', 'Fiction', '....'),
#             ('AUST1842', 'Spider Man', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Available', 'Fiction','....'),
#             ('AUST1243', 'Doctor Strange', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Available', 'Fiction','....'),
#             ('AUST1244', 'Super Man', 'Jane Austen (101)', 'N/A', '1812', '1', '3000', '5900', 'Good', 'Available', 'Fiction','....'),
#             ('AUST1245', 'Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Available', 'Fiction','....'),
#             ('AUST0266', 'One Punch Man', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Available', 'Fiction','....'),
#             ('AUST1856', 'Naruto', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Available', 'Fiction','....'),
#             ('AUST1209', 'Advenger', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold', 'Fiction','....')
#         ]


# book_list = [
#             ('Poor Dad Rich Dad', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold', 'Fiction', '1'), 
#             ('Harry Porter', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold', 'Fiction', '1'), 
#             ('Sense and Sensibility', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold', 'Fiction', '2'), 
#             ('Love', 'Jane Austen (101)', 'N/A', '1812', '1', '3000', '5900', 'Good', 'Sold', 'Fiction', '1'), 
#             ('Dragon Balls', 'Jane Austen (101)', 'N/A', '1811', '1', '3000', '5900', 'Good', 'Sold', 'Fiction', '2')
#             ]


if __name__ == '__main__':
    root = tk.Tk()
    root.state('zoomed')
    app = OrderDetail(root)
    app.render()
    app.pack(fill="both", expand=True)

    app.mainloop()