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
    naming = input("Enter Product Name: ")
    return naming

#Define a function get_quantity()
def get_quantity():
    stock = input('Enter quantity: ')
    return stock
        
def total_quantity():
    total = 0
    try:
        with open("orders.txt","r") as file:
            for line in file:
                parts = line.strip().split(",")
            if len(parts) >= 3:
                qty = int(parts[2].strip())
                total += qty
    except FileNotFoundError:
        return 0
    return total

def generate_report(total_units, failed_attempts):
    print("Total Unit Processed:", total_units ,"|", "No. of rejected entries:", failed_attempts)

def main():

    orders = load_inventory()
    rejected = 0
    print("Current Orders: \n")
    for order in orders:
        print(order)
    
    while True:
     product = product_name()
     quantity = get_quantity()

     if quantity.isdigit() == False:
         print("Invalid no.")
         rejected += 1

     next_id = 1001 + len(orders)
     new_orders = f"{next_id},{product},{quantity}"
     print("New Order Added:\n", new_orders)
     save_inventory(new_orders)

     get_total = total_quantity()

     user_input = input("\nPress Enter to add another order, or type 'quit' to exit: ")
     if user_input.lower() == "quit":
        print(generate_report(get_total, rejected))
        break


main()


