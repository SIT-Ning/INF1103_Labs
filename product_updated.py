from abc import ABC, abstractmethod
from supply import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        self._product_id = product_id
        self.name = name
        self._price = price
        self._stock = stock
        self.supplier: Supplier = supplier
    
    def update_stock(self, quantity: int) -> None:
        self._stock += quantity
        if self._stock < 0: # type: ignore
            self._stock = 0
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Must be implemented by subclasses"""
        pass
    
    def display_information(self) -> None:
        print(f"ID : {self._product_id} | Name: {self.name} | Price: ${self._price:.2f} | Stock: {self._stock}")
        
    @abstractmethod    
    def to_dict(self) -> dict:
        pass