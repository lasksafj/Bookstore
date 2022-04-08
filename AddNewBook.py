from tkinter import *
from PIL import Image, ImageTk

#class ModifyOption:
window = Tk()
window.title("Bookstore")
window.geometry("600x700")
window.iconphoto(True, PhotoImage(file="logo.png"))

# Create text box label
nameOfPage = Label(window, text="Add New Book")
blank = Label(window, text="")
bookID = Label(window, text="BOOK ID")
title = Label(window, text="TITLE")
author = Label(window, text="AUTHOR")
publisher = Label(window, text="PUBLISHER")
publicationDate = Label(window, text="PUBLICATION DATE")
edition = Label(window, text="EDITION")
cost = Label(window, text="COST")
suggestRetailPrice = Label(window, text="SUG RETAIL PRICE")
condition = Label(window, text="CONDITION")
sold = Label(window, text="SOLD")
dateIn = Label(window, text="DATE IN")
dateOut = Label(window, text="DATE OUT")

# Showing label onto the screen
nameOfPage.grid(row=0, column=1)
blank.grid(row=1, column=0)
blank.grid(row=2, column=0)
bookID.grid(row=3, column=0, sticky="w", padx=10)
title.grid(row=4, column=0, sticky="w", padx=10)
author.grid(row=5, column=0, sticky="w", padx=10)
publisher.grid(row=6, column=0, sticky="w", padx=10)
publicationDate.grid(row=7, column=0, sticky="w", padx=10)
edition.grid(row=8, column=0, sticky="w", padx=10)
cost.grid(row=9, column=0, sticky="w", padx=10)
suggestRetailPrice.grid(row=10, column=0, sticky="w", padx=10)
condition.grid(row=11, column=0, sticky="w", padx=10)
sold.grid(row=12, column=0, sticky="w", padx=10)
dateIn.grid(row=13, column=0, sticky="w", padx=10)
dateOut.grid(row=14, column=0, sticky="w", padx=10)

# Create text box entry
bookID = Entry(window, width=50, fg="blue", borderwidth=3, state=DISABLED)
title = Entry(window, width=50, fg="blue", borderwidth=3)
author = Entry(window, width=50, fg="blue", borderwidth=3)
publisher = Entry(window, width=50, fg="blue", borderwidth=3)
publicationDate = Entry(window, width=50, fg="blue", borderwidth=3)
edition = Entry(window, width=50, fg="blue", borderwidth=3)
cost = Entry(window, width=50, fg="blue", borderwidth=3)
suggestRetailPrice = Entry(window, width=50, fg="blue", borderwidth=3)
condition = Entry(window, width=50, fg="blue", borderwidth=3)
sold = Entry(window, width=50, fg="blue", borderwidth=3)
dateIn = Entry(window, width=50, fg="blue", borderwidth=3)
dateOut = Entry(window, width=50, fg="blue", borderwidth=3)

# Show entry onto the screen
bookID.grid(row=3, column=1)
title.grid(row=4, column=1)
author.grid(row=5, column=1)
publisher.grid(row=6, column=1)
publicationDate.grid(row=7, column=1)
edition.grid(row=8, column=1)
cost.grid(row=9, column=1)
suggestRetailPrice.grid(row=10, column=1)
condition.grid(row=11, column=1)
sold.grid(row=12, column=1)
dateIn.grid(row=13, column=1)
dateOut.grid(row=14, column=1)

# Insert comment for entry
title.insert(4, "Enter title of book")

# Create button
cancelButton = Button(window, text="Cancel", pady=5)
saveButton = Button(window, text="Save", padx=10, pady=5)

# Shhow button onto the screen
cancelButton.grid(row=15, column=1, sticky="e", ipadx=10, padx=50)
saveButton.grid(row=15, column=1, sticky="e")


window.mainloop()
