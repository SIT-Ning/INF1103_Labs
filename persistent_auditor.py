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

def save_inventory()