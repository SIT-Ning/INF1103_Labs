import json
import os

#Define load_inventory()
def load_inventory(filename = 'inventory.json'):
    if os.path.exists(filename):
        try:
            with open(filename,"r") as file:
                records = json.load(file)
            print("Inventory loaded successfully.")
        except json.JSONDecodeError:
            records = {}
        return records
    else:
        with open(filename,"w") as file:
            json.dump({}, file)
        return {}

#Define save_inventory()
def save_inventory(new_entry, filename = "inventory.json"):
    with open(filename,"w") as file:
        json.dump(new_entry, file, indent=4)
    print("\nSaving inventory...\n Inventory saved successfully to inventory.json")

#Define add_product()
def add_product(inventory):
    inventory = load_inventory()
    print("Add New Product\n")
    prd_id = input("Product ID: ")
    if prd_id in inventory:
        print (f"Error: Product Id: {prd_id} already exists")
        return
    prd_name = input("Product Name: ")
    price = float(input("Price: $"))
    stock = int(input("Stock quantity: "))

    inventory[prd_id] = {
        "name":prd_name,
        "price":price,
        "stock":stock
    }

    saving = save_inventory(inventory)
    print("Product added successfully!")
    return saving

#Define update_stock()
def update_stock(inventory):
    print("Update stock")
    prd_id = input("Enter Product ID: ")
    inventory = load_inventory()
    if prd_id in inventory:
        product = inventory[prd_id]
        print("Product Found")
        print(f"Name: {product["name"]}")
        print(f"Current Stock: {product["stock"]}\n")

        new_stock = int(input("New stock quantity: "))
        inventory[prd_id]["stock"] = new_stock

        save_inventory(inventory)
        print("\nStock update successfully")
    else:
        print("\nProduct not found")

#Define search_product()
def search_product(inventory):
    print("Search product")
    prd_id = input("Enter Product ID: ")
    inventory = load_inventory()
    if prd_id in inventory:
        product = inventory[prd_id]
        print("\nProduct Found")
        print("---------------------------------")
        print(f"ID: {prd_id}")
        print(f"Name: {product["name"]}")
        print(f"Price: {product["price"]}")
        print(f"Stock: {product["stock"]}")
        print("---------------------------------")
    else:
        print('Product Not Found')

#Define display_all()
def display_all(inventory):
    inventory = load_inventory()
    print("Current Inventory")
    print("---------------------------------")
    for prd_id, details in inventory.items():
        name = details.get("name","")
        price = float(details.get("price",0.0))
        stock = int(details.get("stock",0))

        print(f"ID:{prd_id} | Name:{name} | Price:${price:.2f} | Stock:{stock}")
    print("---------------------------------")

def main():
    print("================================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("================================================")
    print("inventory.json found!")
    inventory = load_inventory()
    while True:
        print("\n--------------MENU-------------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("---------------------------------")

        choice = input("Enter option: ")

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            save_inventory(inventory)
        elif choice == "6":
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.\nProgram Terminated.")
            break
        else:
            print("Enter a number between 1 and 6")

main()


