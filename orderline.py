from product_updated import Product

class OrderLine:
    def __init__(self, product: str, quantity: int) -> None:
        self.product = product
        self.quantity: int = quantity
    
    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity
    
    def display_information(self) -> None:
        print(f"{self.product.name} x{self.quantity} = ${self.calculate_subtotal():.2f}")