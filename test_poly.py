from supply import Supplier
from inventory import Inventory
from physical import PhysicalProduct
from digital import DigitalProduct
from product_updated import Product

supplier = Supplier("S001", "Tom", "tom@example.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.0, 10, 2.5, supplier)
ebook = DigitalProduct("D001", "Ebook", 15.0, 100, 5.0, supplier)

inventory = Inventory()
inventory.add_product(laptop)
inventory.add_product(ebook)

for product in inventory.products:
    product.display_information()
    print(product.get_fulfilment_info())
    print("-" * 40)