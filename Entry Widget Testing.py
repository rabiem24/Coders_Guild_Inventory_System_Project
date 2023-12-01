from tkinter import *
from tkinter import ttk


def submit():
    word = name.get()
    print(word)

root = Tk()
name = StringVar()

entry1 = ttk.Entry(root, textvariable=name).pack()

button1 = ttk.Button(root, text="Submit", command=submit).pack()

root.mainloop()


