from supply import Supplier
from physical import PhysicalProduct
from digital import DigitalProduct
from order import Order

supplier = Supplier("S001", "Tom", "tom@example.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.0, 10, 2.5, supplier)
ebook = DigitalProduct("D001", "Ebook", 15.0, 100, 5.0, supplier)

order1 = Order("O001")
order1.add_order(laptop, 2)
order1.add_order(ebook, 5)
order1.display_information()

order2 = Order("O002")
order2.add_order(laptop, 1)

line1 = order1.order_lines[0]
line2 = order2.order_lines[0]
print("Is same OrderLine Object?:",line1 is line2)
print("Is same Product object?:", line1.product is line2.product)

order1.remove_order("D001")
order1.display_information()
