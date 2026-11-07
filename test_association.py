from supply import Supplier
from physical import PhysicalProduct
from digital import DigitalProduct

supplier = Supplier("S001", "Acme Ltd", "acme@example.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.0, 10, 2.5, supplier)
ebook = DigitalProduct("D001", "Ebook", 15.0, 100, 5.0, supplier)

print("laptop is ebook:       ", laptop is ebook)         
print("laptop is supplier:    ", laptop is supplier)       
print("ids:", id(supplier), id(laptop), id(ebook))         

print("laptop.supplier is supplier:      ", laptop.supplier is supplier)       
print("laptop.supplier is ebook.supplier:", laptop.supplier is ebook.supplier) 

del supplier
laptop.supplier.display_information()
ebook.supplier.display_information()
