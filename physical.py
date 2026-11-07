from canbeshipped import CanBeShipped
from product_updated import Product
from supply import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self._weight = weight
        
    def get_fulfilment_info(self) -> str:
            return "Product requires physical shipping."
    
    def calculate_shipping_cost(self) -> float:
        return self._weight*5.0
    
    def display_information(self) -> None:
        super().display_information()
        print(f"| Weight: {self._weight}kg | Fulfillment: {self.get_fulfilment_info()}")
        print("| Supplier: ", end="")
        self.supplier.display_information()
    
    def to_dict(self) -> dict:
        return {
            "type": "physical",
            "product_id": self._product_id,
            "name": self.name,
            "price": self._price,
            "stock": self._stock,
            "weight": self._weight,
            "supplier": {
                "supplier_id": self.supplier._supplier_id,
                "name": self.supplier._name,
                "contact_email": self.supplier._contact_email
               }
        }