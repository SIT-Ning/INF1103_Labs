from orderline import OrderLine
from product_updated import Product

class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.order_lines : list[OrderLine] = []
        
    def add_order(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)
        
    def remove_order(self, product_id: str) -> None:
        self.order_lines = [line for line in self.order_lines 
                            if line.product.product_id != product_id]
        
    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.order_lines)
    
    def display_information(self) -> None:
        print(f"Order {self.order_id}")
        for line in self.order_lines:
            line.display_information()
        print(f"Total: ${self.calculate_total():.2f}")