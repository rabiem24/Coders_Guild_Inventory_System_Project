from Project101ViewList import tree
import Database
index = 0
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

