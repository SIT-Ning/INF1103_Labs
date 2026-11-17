from product_updated import Product
from digital import DigitalProduct
from physical import PhysicalProduct
from supply import Supplier

class ProductFactory:
    @staticmethod 
    def create(product_type: str, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier) -> Product: 
        if product_type == "physical": 
            return PhysicalProduct(product_id, name, price, stock_quantity, supplier) 
        elif product_type == "digital": 
            return DigitalProduct(product_id, name, price, stock_quantity, supplier) 
        else: 
            raise ValueError(f"Unknown product type: {product_type}")