import os
#Define a function load_inventory()
def load_inventory():
    if os.path.exists("orders.txt"):
        with open("orders.txt", "r") as file:
            read_file = file.read()
            return read_file
    else:
        file = open("orders.txt","w")
    return file

#Define a function save_inventory()
def save_inventory(new_entry):
    for i in new_entry:
        with open("orders.txt", "a") as inventory_update:
            inventory_update.write(i, "\n")

#Define a function product_name()
def product_name():
    naming = input("Enter Product Name: ")
    return product_name

#Define a function get_quantity()
def get_quantity():
    stock = input('Enter quantity: ')
    if stock == "quit":
        return "Quit"
    elif stock.isdigit() == False:
        return "Invalid No."
    else:
        return int(stock)
 
#Print the inventory
current_inventory = load_inventory()
if len(current_inventory) > 0:
    print("Current Inventory:\n")
    for i in current_inventory:
        print(i)
    print("\n")

