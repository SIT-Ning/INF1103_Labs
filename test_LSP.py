from supply import Supplier
from inventory import Inventory
from physical import PhysicalProduct
from digital import DigitalProduct
from product_updated import Product

def show_product_display(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())
    
supplier = Supplier("S001", "Tom", "tom@example.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.0, 10, 2.5, supplier)
ebook = DigitalProduct("D001", "Ebook", 15.0, 100, 5.0, supplier)

show_product_display(laptop)
show_product_display(ebook)

inventory = Inventory()
inventory.add_product(laptop)
inventory.add_product(ebook)
inventory.display_all()
inventory.find_product("P001").update_stock(-5)
inventory.find_product("D001").update_stock(-5)
inventory.display_all()
