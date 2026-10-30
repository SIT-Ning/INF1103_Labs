import json
from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self._price = price
        self._stock = stock
    
    def update_stock(self, quantity):
        self._stock += quantity
        if self._stock < 0:
            self._stock = 0
    @abstractmethod
    def get_fulfilment_info(self):
        """Must be implemented by subclasses"""
        pass
    
    def display_information(self):
        print(f"ID : {self.product_id} | Name: {self.name} | Price: ${self._price:.2f} | Stock: {self._stock}")
        
    @abstractmethod    
    def to_dict(self):
        pass
        
class Inventory:
    def __init__(self):
        self.products = []
    
    def add_products(self, product):
        self.products.append(product)
        
    def search_products(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
    
    def display_all(self):
        if not self.products:
            print('Inventory is empty')
        for product in self.products:
            product.display_information()
    
    def save_to_json(self, filename = "inventory.json"):
        data = [product.to_dict() for product in self.products]
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Inventory saved successfully to {filename}")
    
    def load_from_json(self, filename = "inventory.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.products = []
                for item in data:
                    if item["type"] == "physical":
                        prod = PhysicalProduct(item["product_id"], item["name"], item["price"], item["stock"], item["weight"])
                    elif item["type"] == "digital":
                        prod = DigitalProduct(item["product_id"], item["name"], item["price"], item["stock"], item["download size"])
                    self.products.append(prod)
                print("inventory.json found")
                print(f"Inventory is loaded successfully from {filename}")
        except FileNotFoundError:
            print(f"{filename} is not found. Starting with an empty inventory")

class PhysicalProduct:
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.weight = weight
        
    def get_fulfilment_info(self):
            return "Product requires physical shipping."[cite: 23]
    
    def calculate_shipping_cost(self):
        return self.weight*5.0
    
    def display_information(self):
        super().display_information(self)
        print(f"| Weight: {self.weight}kg | Fulfillment: {self.get_fulfilment_info()}")
    
    def to_dict(self):
        return {
            "type": "physical",
            "product_id": self._product_id,
            "name": self.name,
            "price": self._price,
            "stock": self._stock,
            "weight": self.weight
        }
    
class DigitalProduct:
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.download_size = download_size
    
    def get_fulfilment_info(self):
        return "Product requires physical shipping."[cite: 23]
    
    def display_information(self):
        super().display_information(self)
        print(f"| Weight: {self.download_size}MB | Fulfillment: {self.get_fulfilment_info()}")
    
    def to_dict(self):
        return {"type": "digital", "product_id": self._product_id, "name": self.name, "price": self._price, "stock": self._stock, "download size": self.download_size}

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
                new_product = PhysicalProduct(p_id, p_name, p_price, p_stock, weight)
            else:
                download_size = float(input("Download size(MB): "))
                new_product = DigitalProduct(p_id, p_name, p_price, p_stock, download_size)
            
            inventory.add_products(new_product)
            print("Product added successfully")
        elif choice == "3":
            print("\nUpdate stock")
            p_id = input("Enter Product ID: ")
            product = inventory.search_product(p_id)
            if product:
                print(f"Product Found: \nName: {product.name}\nCurrent stock: {product._stock}")
                new_stock = int(input("Enter new stock quantity: "))
                product.update_stock(new_stock)
                print("Stock quantity updated successfully")
            else:
                print("Product not found.")
        elif choice == "4":
            p_id = input("Product ID: ")
            product = inventory.search_inventory(p_id)
            if product:
                print("\nProduct found!")
                print("-" * 40)
                product.display_information()
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