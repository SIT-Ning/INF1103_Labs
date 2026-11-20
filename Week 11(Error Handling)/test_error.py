from supply import Supplier
from inventory import Inventory
from product_factory import ProductFactory
from input import load_products

def check(description, passed):
    if passed:
        print("PASS |", description)
    else:
        print("FAIL |", description)


supplier = Supplier("S001", "Tom", "tom@example.com")

try:
    ProductFactory.create("service", "S1", "Install", 30.0, 5, supplier)
    check("unknown product type is rejected", False)
except ValueError as error:
    check("unknown product type is rejected with a clear message",
          "Unknown product type" in str(error))
    

print()
print("--- loading products.csv ---")
inventory = Inventory()
load_products("products.csv", inventory, supplier)
print("--- done ---")
print()

ids = []
for p in inventory.products:
    ids.append(p.product_id)
check("only the 3 valid products were loaded: " + str(ids), ids == ["P001", "D001", "P003"])


print()
print("--- loading a file that does not exist ---")
empty_inventory = Inventory()
load_products("no_such_file.csv", empty_inventory, supplier)
print("--- done ---")
print()
check("program did not crash and inventory is empty", len(empty_inventory.products) == 0)