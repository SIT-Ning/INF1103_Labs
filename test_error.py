from inventory import Inventory
from supply import Supplier
from input import load_products

inv = Inventory()
load_products("products.csv", inv, Supplier("S001", "Tom", "tom@example.com"))
print("IDs in inventory:", [p.product_id for p in inv.products])