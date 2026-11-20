from supply import Supplier
from product_factory import ProductFactory
from orderline import OrderLine
from discount import PercentageDiscount

def check(description, passed):
    if passed:
        print("PASS | ", description)
    else:
        print("FAIL | ", description)


supplier = Supplier("S001", "Tom", "tom@example.com")

try:
    ProductFactory.create("physical", "P1", "Lamp", 0, 5, supplier)
    check("price 0 is rejected", False)
except ValueError:
    check("price 0 is rejected", True)
    
try:
    ProductFactory.create("physical", "P1", "Lamp", -5, 5, supplier)
    check("price 0 is rejected", False)
except ValueError:
    check("price 0 is rejected", True)
    
try:
    ProductFactory.create("digital", "D1", "Ebook", 0, 5, supplier)
    check("price 0 is rejected for a digital product", False)
except ValueError:
    check("price 0 is rejected for a digital product", True)
    

try:
    ProductFactory.create("physical", "P1", "Lamp", 10.0, -1, supplier)
    check("negative stock is rejected", False)
except ValueError:
    check("negative stock is rejected", True)
    
try:
    ProductFactory.create("physical", "P1", "Lamp", 10.0, 0, supplier)
    check("stock 0 is allowed", False)
except ValueError:
    check("stock 0 is allowed", True)
    

product = ProductFactory.create("physical", "P2", "Chair", 40.0, 5, supplier)
try:
    OrderLine(product, 0)
    check("quantity 0 is rejected", False)
except ValueError:
    check("quantity 0 is rejected", True)

try:
    OrderLine(product, -3)
    check("negative quantity is rejected", False)
except ValueError:
    check("negative quantity is rejected", True)
    
    
try:
    PercentageDiscount(150)
    check("discount of 150% is rejected", False)
except ValueError:
    check("discount of 150% is rejected", True)