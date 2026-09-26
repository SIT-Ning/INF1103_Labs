import os

def load_inventory():
    if os.path.exists("orders.txt"):
        with open("orders.txt", "r") as file:
            # Read all non-empty lines into a list
            orders = [line.strip() for line in file if line.strip()]
            return orders
    return []

def save_inventory(new_entry):
    # Append the new formatted order string to the file
    with open("orders.txt", "a") as file:
        file.write(new_entry + "\n")
    print("Order successfully saved to orders.txt")

def get_product_name():
    naming = input("Enter Product Name: ")
    return naming

def get_quantity():
    stock = input("Enter Quantity: ")
    if stock.lower() == "quit":
        return "Quit"
    elif not stock.isdigit():
        return "Invalid No."
    else:
        return int(stock)

# --- Main Program Execution ---

# 1. Load existing orders
orders = load_inventory()

# 2. Display current orders
print("Current Orders:\n")
if orders:
    for order in orders:
        print(order)
    print()  # Blank line for spacing
else:
    print("No existing orders found.\n")

# 3. Determine next Order ID (starts at 1001 if file is empty)
next_id = 1001
if orders:
    last_order = orders[-1]
    # Extract ID from the first field of the comma-separated string
    last_id = int(last_order.split(',')[0])
    next_id = last_id + 1

# 4. Get input from user
product = get_product_name()
quantity = get_quantity()

# 5. Process valid entry
if quantity not in ["Quit", "Invalid No."]:
    # Format order entry (e.g., "1004,Laptop Stand,2")
    new_order_str = f"{next_id},{product},{quantity}"
    
    print("\nNew Order Added:")
    print(new_order_str)
    print()
    
    # Save entry to orders.txt
    save_inventory(new_order_str)
elif quantity == "Invalid No.":
    print("Invalid quantity entered.")