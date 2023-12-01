from tkinter import *
import Database






def inventory():
    inventory_screen = Tk()
    inventory_screen.title("Inventory")
    global tree
    TopViewForm = Frame(inventory_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(inventory_screen, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(inventory_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Products", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("ProductID", "Product Name", "Product Qty", "Product Price"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('ProductID', text="ProductID",anchor=W)
    tree.heading('Product Name', text="Product Name",anchor=W)
    tree.heading('Product Qty', text="Product Qty",anchor=W)
    tree.heading('Product Price', text="Product Price",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()

def show_costumer_form():
    dashboard.destroy()
    addCostumerForm()


def addCostumerForm():

    screen = Tk()
    screen.geometry("500x500")
    screen.title("First Project")
    screen.configure(background="#FFEAAC")

    # Text Label
    heading = Label(screen, text="Add Customer", fg="black", bg="#E8A66D", width="500", height="3").pack()
    Label(screen, text="Customer:", bg="#FFEAAC").place(x=50, y=80)
    Label(screen, text="Contact:", bg="#FFEAAC").place(x=73, y=120)
    Label(screen, text="Address:", bg="#FFEAAC").place(x=60, y=160)
    Label(screen, text="Item Order:", bg="#FFEAAC").place(x=60, y=200)
    Label(screen, text="Quantity:", bg="#FFEAAC").place(x=60, y=200)


    # Customer Entry
    costumer_entry = Entry(screen).place(x=110, y=80)

    # Email Entry
    contact_no = Entry(screen).place(x=110, y=120)

    # Contact Number Entry
    address_field = Entry(screen).place(x=110, y=160)

    # Address Entry
    item_order = Entry(screen).place(x=110, y=200)

    # Address Entry
    item_quantity = Entry(screen).place(x=110, y=200)

    # Cutomer StringVar
    customer = StringVar()
    customer.get(costumer_entry)
    # Email StringVar
    contacts = StringVar()
    contacts.get(contact_no)
    # Contact StringVar
    address = StringVar()
    address.get(address_field)
    # Item
    item = IntVar()
    item.get(item_order)
    # Quantity
    item_quantity = IntVar()
    item_quantity.get(item_quantity)

    # submit button
    submit_button = Button(screen, text="Submit", bg="#E8A66D").place(x=110, y=285)

def submit():
    costumer_add(customer, contacts, address, item, item_quantity)

def main():
    root = Tk()
    root.title("Inventory System")

    heading = Label(root, text="Inventory System")
    heading.grid(row=0, column=1, columnspan=2, sticky="WE")

    customer_button = Button(root, text="Customer Order", command=addCostumerForm)
    customer_button.grid(row=1, column=0)

    inventory_button = Button(root, text="Inventory", command=inventory)
    inventory_button.grid(row=1, column=1)

    invoice_button = Button(root, text="Invoice")
    invoice_button.grid(row=1, column=2)
    return root



dashboard = main()

dashboard.mainloop()