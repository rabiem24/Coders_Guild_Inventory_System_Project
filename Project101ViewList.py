from tkinter import *
import tkinter as tk
from tkinter import ttk
import Database

##### Methods #####

def item_count(item, quantity):
    cur_item = tree.focus()
    contents = tree.item(cur_item)
    selected_item = contents['values']



def remove_item():
    # Ge
    cur_item = tree.focus()
    contents = tree.item(cur_item)
    selected_item = contents['text']
    Database.remove_item(selected_item)
    tree.delete(cur_item)


def update_list():
    view = Database.get_item_list()
    for data in view:
        tree.insert('', 'end', text=data[0], values=data[1:])






#### GUI #####

root = Tk()
root.title("Main Page")
root.geometry("1300x700")
root.configure(bg='#FFEAAC')


tk.Label(root, text="View List",fg = "white",bg = "#E8A66D",font='times 35 bold',width = "500",height = "1").pack()
#Top Frame
topframe = Frame(root, width=1300, height=50, bd=3,bg='#FFEAAC')
topframe.pack(side=TOP)
#------------------------------------------------------------------------------------
#Inside Top Frame
#Left Frame
leftmidframe = Frame(topframe, width=650, height=50, bg='#FFEAAC')
leftmidframe.pack(side=LEFT)

#------------------------------------------------------------------------------------
#Right Frame
rightmidframe = Frame(topframe, width=650, height=50,bg='#FFEAAC')
rightmidframe.pack(side=RIGHT)
#Inside Right Frame
rightframe = Frame(rightmidframe, width=206, height=50, bg='#FFEAAC')
rightframe.pack(side=RIGHT)
midframe = Frame(rightmidframe, width=206, height=50, bg='#FFEAAC')
midframe.pack(side=LEFT)
#-------------------------------------------------------------------------------------
#Search Frame
searchframe = Frame(rightmidframe, width=206, height=50, bg='#FFEAAC')
searchframe.pack(side=RIGHT)
#Search Divided Frame
search1 = Frame(searchframe, width=56, height=50, bg='#FFEAAC')
search1.pack(side=RIGHT)
search2 = Frame(searchframe, width=150, height=50, bg='#FFEAAC')
search2.pack(side=LEFT)
#Search Button
search_label = Button(search1, text="Search", font='times 10 bold',padx=15, bd=1, relief='raise')
search_label.pack()
#Search Entry
searchstore = StringVar()
search_entry = Entry(rightframe, text="",textvariable=searchstore,width=20)
search_entry.pack(padx=10)

#------------------------------------------------------------------------------------
#StringVar Button
additem = StringVar()
removeitem = StringVar()
bill = StringVar()
generatereport = StringVar()
customerorder= StringVar()

#Add Button
add_item_button = Button(leftmidframe, text="Add Item", font='times 10 bold', bd=2, relief='raise' )
add_item_button.grid(row=0,column=0,padx=2)

#Remove Button
remove_Item_button = Button(leftmidframe, text="Remove Item", font='times 10 bold', bd=2, relief='raise',\
                            command=remove_item)
remove_Item_button.grid(row=0,column=1,padx=2)

#Bill Button
bill_button = Button(leftmidframe, text="Bill", font='times 10 bold', bd=2, relief='raise', width=5)
bill_button.grid(row=0,column=2,padx=2)

#Generate Button
generate_report_button = Button(leftmidframe, text="Generate Report", font='times 10 bold', bd=2, relief='raise',\
                                width=15, command=update_list)
generate_report_button.grid(row=0,column=3,padx=2)

#Customer Order Button
customer_order_button = Button(leftmidframe, text="Customer Order", font='times 10 bold', bd=2, relief='raise',\
                               width=15)
customer_order_button.grid(row=0,column=4,padx=2)

#hide label
hide_label = Label(leftmidframe,bg="#FFEAAC", width=30)
hide_label.grid(row=0,column=5,padx=2)

#-------------------------------------------------------------------------------------
#Frame
inventoryframe = Frame(root, width=1350, height=750, bd=2, relief='raise')
inventoryframe.pack(side=TOP)


#---------------------------------------------
tree = ttk.Treeview(inventoryframe)
tree["columns"] = ("one", "two", "three", "four", "five", "six", "seven")
tree.column("#0", width=170, minwidth=100, stretch="YES")
tree.column("one", width=170, minwidth=100, stretch="YES")
tree.column("two", width=220, minwidth=100)
tree.column("three", width=100, minwidth=100, stretch="YES")
tree.column("four", width=100, minwidth=100, stretch="YES")
tree.column("five", width=150, minwidth=100, stretch="YES")
tree.column("six", width=150, minwidth=100, stretch="YES")
tree.column("seven", width=150, minwidth=100, stretch="YES")

tree.heading("#0", text="Item ID", anchor="w")
tree.heading("one", text="Item Description", anchor="w")
tree.heading("two", text="Item Type", anchor="w")
tree.heading("three", text="Qty", anchor="w")
tree.heading("four", text="Cost", anchor="w")
tree.heading("five", text="Customer", anchor="w")
tree.heading("six", text="Quantity Ordered", anchor="w")
tree.heading("seven", text="Bill", anchor="w")

tree.pack(pady=100)
#---------------------------------------------


root.mainloop()
