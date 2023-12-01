from tkinter import *
from tkinter import ttk
import Database

###### GLOBAL VARIABLES ######

def main_menu():
    global screen1
    screen.withdraw()
    screen1 = Tk()
    screen1.title("Main Page")
    screen1.geometry("1300x700")
    screen1.configure(bg='#FFEAAC')

    Label(screen1,text="Main Menu",fg = "white",bg = "#E8A66D",font='times 35 bold',width = "500",height = "1").pack()
    headingline = Frame(screen1, width=1300, height=5, bd=3,bg="#FF9380")
    headingline.pack(side=TOP)
    #Top Frame
    topframe = Frame(screen1, width=1300, height=50, bd=3,bg='#FFEAAC')
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
    #Search StringVar
    searchstore = StringVar()

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
    search_entry = Entry(rightframe,text="",textvariable=searchstore,width=20)
    search_entry.pack(padx=10)
    #------------------------------------------------------------------------------------


    #Add Button
    add_item_button = Button(leftmidframe,text="Add Item", font='times 10 bold', bd=2, relief='raise', command=add_item)
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
    customer_order_button = Button(leftmidframe, text="Customer Order", font='times 10 bold', bd=2, relief='raise', width=15, command=order)
    customer_order_button.grid(row=0,column=4,padx=2)

    #hide label
    hide_label = Label(leftmidframe,bg="#FFEAAC", width=30)
    hide_label.grid(row=0,column=5,padx=2)

    #-------------------------------------------------------------------------------------
    #Frame
    inventoryframe = Frame(screen1, width=1350, height=750, bd=2, relief='raise')
    inventoryframe.pack(side=TOP)


    #---------------------------------------------
    global tree
    tree = ttk.Treeview(inventoryframe)
    tree["columns"] = ("one", "two", "three", "four","five","six","seven")
    tree.column("#0", width=150, minwidth=100, stretch="YES")
    tree.column("one", width=170, minwidth=100, stretch="YES")
    tree.column("two", width=220, minwidth=100)
    tree.column("three", width=100, minwidth=100, stretch="YES")
    tree.column("four", width=100, minwidth=100, stretch="YES")
    tree.column("five", width=150, minwidth=100, stretch="YES")
    tree.column("six", width=150, minwidth=100, stretch="YES")

    tree.heading("#0", text="Item ID", anchor="w")
    tree.heading("one", text="Item Description", anchor="w")
    tree.heading("two", text="Item Type", anchor="w")
    tree.heading("three", text="Qty", anchor="w")
    tree.heading("four", text="Cost", anchor="w")
    tree.heading("five", text="Customer", anchor="w")
    tree.heading("six", text="Quantity Ordered", anchor="w")
    tree.heading("seven", text="Bill", anchor="w")

    tree.pack(pady=100)
    update_list()
   

def add_item():
    global screen2
    screen2 = Tk()
    screen2.title("Add Item")
    screen2.geometry("600x600")
    screen2.configure(bg='#FFEAAC')
    screen2.resizable(False, False)

    Label(screen2,text="Add Item",fg = "white",bg = "#E8A66D",font='times 35 bold',width = "500",height = "1").pack()
    headingline = Frame(screen2, width=600, height=5, bd=3,bg="#FF9380")
    headingline.pack(side=TOP)
    #Frame
    firstframe = Frame(screen2, width=600,bg="grey", height=520, bd=1, relief='raise')
    firstframe.place(x = 0, y = 100)
    #Inside Frame
    firstframe = Frame(screen2, width=250, height=520, bd=2, relief='raise')
    firstframe.place(x = 2, y = 102)
    secondframe = Frame(screen2, width=350, height=520, bd=2, relief='raise')
    secondframe.place(x = 253, y = 102)

    #label And Entry
    label1= Label(screen2,text="Item ID:", font='calibri 25 ').place(x = 5, y = 150)
    label2= Label(screen2,text="Item Description:", font='calibri 25 ').place(x = 5, y = 200)
    label3= Label(screen2,text="Item Type:", font='calibri 25 ').place(x = 5, y = 250)
    label4= Label(screen2,text="Qty:", font='calibri 25 ').place(x = 5, y = 300)
    label5= Label(screen2,text="Cost:", font='calibri 25 ').place(x = 5, y = 350)

    global item_id
    global item_description
    global item_type
    global item_qty
    global item_cost
    itemid = StringVar()
    itemdescription = StringVar()
    itemtype = StringVar()
    qty = IntVar()
    cost = DoubleVar()

    item_id.get(itemid)
    item_description.get(itemdescription)
    item_type.get(itemtype)
    item_qty.get(qty)
    item_cost.get(cost)

    entry1 = Entry(screen2, textvariable=itemid, width=20,bg="white",font='calibri 18 ').place(x = 270, y = 155 )
    entry2 = Entry(screen2, textvariable=itemdescription, width=20,bg="white",font='calibri 18 ').place(x = 270, y = 205 )
    entry3 = Entry(screen2, textvariable=itemtype, width=20,bg="white",font='calibri 18 ').place(x = 270, y = 255 )
    entry4 = Entry(screen2, textvariable=qty, width=20,bg="white",font='calibri 18 ').place(x = 270, y = 300 )
    entry5 = Entry(screen2, textvariable=cost, width=20,bg="white",font='calibri 18 ').place(x = 270, y = 350 )

    #Submit Button
    submit = Button(screen2, text="Submit",bg="lightgreen", font='times 18 bold', width=17,\
                    command=submit_item)
    submit.place(x = 270, y = 395)
    return item_id, item_description, item_type, item_qty, item_cost
    
def order():
    global screen3
    screen3 = Tk()
    screen3.title("Customer Order")
    screen3.geometry("500x500")
    screen3.configure(bg='#FFEAAC')
    screen3.resizable(False, False) 
    Label(screen3,text="Customer Order",fg = "white",bg = "#E8A66D",font='times 35 bold',width = "500",height = "1").pack()
    headingline = Frame(screen3, width=600, height=5, bd=3,bg="#FF9380")
    headingline.pack(side=TOP)
    #Frame
    firstframe = Frame(screen3, width=600,bg="grey", height=520, bd=1, relief='raise')
    firstframe.place(x = 0, y = 100)
    #Inside Frame
    firstframe = Frame(screen3, width=150, height=500, bd=2, relief='raise')
    firstframe.place(x = 2, y = 102)
    secondframe = Frame(screen3, width=350, height=500, bd=2, relief='raise')
    secondframe.place(x = 152, y = 102)
    #StringVar
    global costumername
    global costumeritemid
    global costumerqty
    costumername = StringVar()
    costumeritemid = StringVar()
    costumerqty = IntVar()


    #label And Entry
    label1= Label(screen3,text="Name:", font='calibri 25 ').place(x = 5, y = 150)
    label2= Label(screen3,text="Order:", font='calibri 25 ').place(x = 5, y = 200)
    label3= Label(screen3,text="Qty:", font='calibri 25 ').place(x = 5, y = 250)

    entry1 = Entry(screen3, textvariable=costumername, width=20,bg="white",font='calibri 18 ').place(x = 175, y = 155 )
    entry2 = Entry(screen3, textvariable=costumeritemid, width=20,bg="white",font='calibri 18 ').place(x = 175, y = 205 )
    entry3 = Entry(screen3, textvariable=costumerqty, width=20,bg="white",font='calibri 18 ').place(x = 175, y = 255 )
    #Submit Button
    submit = Button(screen3, text="Submit",bg="lightgreen", font='times 18 bold', width=17, command=screen3.destroy)
    submit.place(x = 175, y = 320)

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("500x500")
    screen.title("Login Page")
    screen.configure(background="#FFEAAC")
    screen.resizable(False, False)
    heading = Label(text = "Small Inventory System", fg = "white", bg = "#E8A66D",width="500", height ="1",font='times 35 bold').pack()
    headingline = Frame(screen, width=500, height=5, bd=3,bg="#FF9380")
    headingline.pack(side=TOP)

    #Frame
    topframe = Frame(screen, width=400, height=400, bd=3, relief='raise')
    topframe.place(x = 50, y = 94)

    #Title Name Login
    Label(text= "Login", font='times 25 bold').place(x = 200, y = 120)
    #Label
    Label(text= "USERNAME:", font='times 20 bold').place(x = 60, y = 220)
    Label(text= "PASSWORD:", font='times 20 bold').place(x = 60, y = 270)
    #Login
    user_name = StringVar()
    password = StringVar()
    username_entry = Entry(screen, textvariable=user_name, width=20,bg="white", font='times 15 bold').place(x = 228, y = 225 )
    username_entry = Entry(screen, textvariable=password, width=20,bg="white", font='times 15 bold').place(x = 228, y = 277 )
    #--------------------------------------------
    submit = Button(screen, text="Confirm",bg="lightgreen", font='times 18 bold',command=main_menu, width=25)
    submit.place(x = 70, y = 340)
    return screen


log_in = main_screen()



#### METHODS ####

def submit_item():
    results = add_item()
    #Database.add_item(item_id, item_description, item_type, item_qty, item_cost)
    print(results)

    screen2.withdraw()



def remove_item():

    cur_item = tree.focus()
    contents = tree.item(cur_item)
    selected_item = contents['text']
    Database.remove_item(selected_item)
    tree.delete(cur_item)


def update_list():
    view = Database.get_item_list()
    for data in view:
        tree.insert('', 'end', text=data[0], values=data[1:])

def submit_costumer():
    costumer_name = costumername.get().strip.title()
    costumer_item_order = costumeritemid.get().strip()
    costumer_order_qty = costumerqty.get()

    Database.add_costumer_order(costumer_name, costumer_item_order, costumer_order_qty)

log_in.mainloop()

