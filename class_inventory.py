import json
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self._price = price
        self._stock = stock
    
    def update_stock(self, quantity):
        self._stock += quantity
        if self._stock < 0:
            self._stock = 0
    
    def display_information(self):
        print(f"ID : {self.product_id} | Name: {self.name} | Price: ${self._price:.2f} | Stock: {self._stock}")
        
    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self._price,
            "stock": self._stock
        }

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
                self.products = [
                    Product(item["product_id"], item["name"], item["price"], item["stock"])
                    for item in data
                ]
                print(f"Inventory is loaded successfully from {filename}")
        except FileNotFoundError:
            print(f"{filename} is not found. Starting with an empty inventory")

# Example inside your main program loop
inventory = Inventory()

# When adding a product from user input:
product1 = Product("P001", "Laptop", 1200.00, 15)
product2 = Product("P002", "Mouse", 25.50, 40)
product3= Product("P004", "Monitor", 299.99, 10)
inventory.add_products(product1)
inventory.add_products(product2)
inventory.add_products(product3)

# When displaying products:
inventory.display_all()
inventory.save_to_json()
inventory.load_from_json()
    