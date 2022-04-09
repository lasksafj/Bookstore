from tkinter import *
import tkinter as tk


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mr.Flinch Bookstore")
        self.state("zoomed")
        self.render()
        
    def render(self):
         
        labelTitle = tk.Label(self, text="BOOK ORDER", fg="red", font=('Arial',16,'bold'))
        labelTitle.grid(row=0, column=0)

        # code for creating table
        self.e = Entry(self, width=20, fg='green', font=('Arial',16,'bold'))     
        self.e.grid(row=1, column=0)
        self.e.insert(END, 'Title')
        self.e = Entry(self, width=20, fg='green', font=('Arial',16,'bold'))
        self.e.grid(row=1, column=1)
        self.e.insert(END, 'Author')
        self.e = Entry(self, width=20, fg='green', font=('Arial',16,'bold'))
        self.e.grid(row=1, column=2)
        self.e.insert(END, 'Published Year')
        self.e = Entry(self, width=20, fg='green', font=('Arial',16,'bold'))
        self.e.grid(row=1, column=3)
        self.e.insert(END, 'Edition')
        self.e = Entry(self, width=20, fg='green', font=('Arial',16,'bold'))
        self.e.grid(row=1, column=4)
        self.e.insert(END, 'Price')

        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(self, width=20, fg='black', font=('Arial',16,'bold'))
                self.e.grid(row=i+2, column=j)
                self.e.insert(END, bookData[i][j])

        labelTitle = tk.Label(self, text="SHOPPING CART", fg="red", font=('Arial',16,'bold'))
        labelTitle.grid(row=20, column=0)
 
# take the data
bookData = [
            ["Northanger Abbey", "Austen, Jane", 1814, "Penguin", 18.2],
            ["War and Peace", "Tolstoy, Leo", 1865, "Penguin", 12.7],
            ["Anna Karenina", "Tolstoy, Leo", 1875, "Penguin", 13.5],
            ["Mrs. Dalloway", "Woolf, Virginia", 1925, "Harcourt Brace", 25],
            ["The Hours", "Cunnningham, Michael", 1999, "Harcourt Brace", 12.35],
            ["Huckleberry Finn", "Twain, Mark", 1865, "Penguin", 5.76],
            ["Bleak House", "Dickens, Charles", 1870, "Random House", 5.75],
            ["Tom Sawyer", "Twain, Mark", 1862, "Random House", 7.75],
            ["A Room of One's Own", "Woolf, Virginia", 1922, "Penguin", 29],
            ["Harry Potter", "Rowling, J.K.", 2000, "Harcourt Brace", 19.95],
            ["One Hundred Years of Solitude", "Marquez", 1967, "Harper  Perennial", 14.00],
            ["Hamlet, Prince of Denmark", "Shakespeare", 1603, "Signet  Classics", 7.95],
            ["Lord of the Rings", "Tolkien, J.R.", 1937, "Penguin", 27.45]
        ]
  
# find total number of rows and
# columns in list
total_rows = len(bookData)
total_columns = len(bookData[0])
  
if __name__ == "__main__":
    app = View()
    app.mainloop()