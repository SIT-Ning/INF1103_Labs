class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self._price = price
        self._stock = stock
    
    def update_stock(self, quantity):
        self._stock += quantity
        if self._stock < 0:
            self._stock = 0
    
    def display_information(self):
        print(f"ID : {self.product_id} | Name: {self.name} | Price: ${self._price:.2f} | Stock: {self._stock}")
        
    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self._price,
            "stock": self._stock
        }
    