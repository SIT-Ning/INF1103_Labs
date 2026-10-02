import json
import os

#Define load_inventory()
def load_inventory(filename = 'inventory.json'):
    if os.path.exists(filename):
        try:
            with open(filename,"r") as file:
                records = json.load(file)
        except json.JSONDecodeError:
            records = {}
        return records
    else:
        inventory = {}
        with open(filename,"a") as file:
            json.dump(inventory, file)
        return inventory

#Define save_inventory()
def save_inventory(new_entry, filename = "inventory.json"):
    with open(filename,"w") as file:
        json.dump(new_entry, file)
    print("\nSaving inventory\n Inventory saved to inventory.json")

#Define add_product()
def add_product():
    prd_id = input("Product ID: ")
    prd_name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock quantity: "))
    return prd_id, prd_name, price, stock

#Define update_stock()
def update_stock():
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

update_stock()

#Define search_product()
def search_product():
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
def display_all():
    inventory = load_inventory()
    print("Current Inventory")
    print("---------------------------------")
    for prd_id, details in inventory.items():
        name = details.get("name","")
        price = float(details.get("price",0.0))
        stock = int(details.get("stock",0))

        print(f"ID:{prd_id} | Name:{name} | Price:{price:.2f} | Stock:{stock}")

    print("---------------------------------")
