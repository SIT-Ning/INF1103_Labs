from physical import PhysicalProduct
from digital import DigitalProduct
from inventory import Inventory
from supply import Supplier
from canbeshipped import CanBeShipped

# Example inside your main program loop
def main():
    inventory = Inventory()
    inventory.load_from_json()
    print("=" * 25)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 25)
    print("inventory.json found!")
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
            print("\nCurrent Directory:")
            inventory.display_all()
        elif choice == "2":
            print("\nAdd new product")
            p_type = input("Product Type: (1: Physical, 2: Digital): ")
            p_id = input("Product ID: ")
            p_name = input("Name: ")
            p_price = float(input("Price: $"))
            p_stock = int(input("Stock Quantity: "))
            
            if p_type == "1":
                weight = float(input("Weight(kg): "))
                supplier = Supplier.supply_input()
                new_product = PhysicalProduct(p_id, p_name, p_price, p_stock, weight, supplier)
            elif p_type == "2":
                download_size = float(input("Download size(MB): "))
                supplier = Supplier.supply_input()
                new_product = DigitalProduct(p_id, p_name, p_price, p_stock, download_size, supplier)
            else:
                continue
                    
            inventory.add_product(new_product)
            print("Product added successfully")
        elif choice == "3":
            print("\nUpdate stock")
            p_id = input("Enter Product ID: ")
            product = inventory.find_product(p_id)
            if product:
                print(f"Product Found: \nName: {product.name}\nCurrent stock: {product._stock}")
                new_stock = int(input("Enter new stock quantity: "))
                product.update_stock(new_stock)
                print("Stock quantity updated successfully")
            else:
                print("Product not found.")
        elif choice == "4":
            p_id = input("Product ID: ")
            product = inventory.find_product(p_id)
            if product:
                print("\nProduct found!")
                print("-" * 40)
                product.display_information()
                print("Supplier")
                supplier.display_information()
                if isinstance(product, CanBeShipped):
                    print(f"Shipping cost: {product.calculate_shipping_cost():.2f}")
                print("-" * 40)
            else:
                print("Product not found")
        elif choice == "5":
            print("\nSaving inventory before exit....")
            inventory.save_to_json()
        elif choice == "6":
            print("\nSaving inventory before exit...")
            inventory.save_to_json()
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please choose between 1 to 6.")

if __name__ == "__main__":
    main()