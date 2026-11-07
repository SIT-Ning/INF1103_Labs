from product_updated import Product
from physical import PhysicalProduct
from digital import DigitalProduct
import json
from supply import Supplier
class Inventory:
    def __init__(self) -> None:
        self.products = []
    
    def add_product(self, product: Product) -> None:
        self.products.append(product)
        
    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
    
    def display_all(self) -> None:
        if not self.products:
            print('Inventory is empty')
        for product in self.products:
            product.display_information()
    
    def save_to_json(self, filename: str = "inventory.json") -> None:
        data = [product.to_dict() for product in self.products]
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Inventory saved successfully to {filename}")
    
    def load_from_json(self, filename: str = "inventory.json") -> None:
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.products = []
                for item in data:
                    s = item["supplier"]
                    supplier = Supplier(s["supplier_id"], s["name"], s["contact_email"])
                    
                    if item["type"] == "physical":
                        prod = PhysicalProduct(item["product_id"], item["name"], item["price"], item["stock"], item["weight"], supplier)
                    elif item["type"] == "digital":
                        prod = DigitalProduct(item["product_id"], item["name"], item["price"], item["stock"], item["download size"], supplier)
                    else:
                        continue
                    self.products.append(prod)
                print("inventory.json found")
                print(f"Inventory is loaded successfully from {filename}")
        except FileNotFoundError:
            print(f"{filename} is not found. Starting with an empty inventory")