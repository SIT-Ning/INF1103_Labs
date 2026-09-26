import os
#Define a function load_inventory()
def load_inventory():
    try:
        with open("orders.txt","r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

#Define a function save_inventory()
def save_inventory(new_entry):
    with open("orders.txt", "a") as inventory_update:
            inventory_update.write(new_entry + "\n")
    print("Orders successfully saved to orders.txt")

#Define a function product_name()
def product_name():
    prd = input("Enter Product Name: ")
    return prd

#Define a function get_quantity()
def get_quantity():
    stock = input('Enter quantity: ')
    if stock.isdigit() == False:
        print("Invalid no.")
    return stock
        

def main():
    orders = load_inventory()
    next_id = 1001
    print("Current Orders: \n")
    for order in orders:
        print(order)
    while True:

        product = product_name()
        quantity = get_quantity()

        new_orders = f"{next_id},{product},{quantity}"
        print("New Order Added:\n", new_orders)
        save_inventory(new_orders)

        user_choice = input("\nDo you want to quit: ")
        if user_choice.lower() == "quit":
            break
        else:
            next_id += 1
            continue

main()


