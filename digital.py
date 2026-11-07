from product_updated import Product
from supply import Supplier 

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self._download_size = download_size
    
    def get_fulfilment_info(self) -> str:
        return "Product is delivered digitally."
    
    def display_information(self) -> None:
        super().display_information()
        print(f"| Download size: {self._download_size}MB | Fulfillment: {self.get_fulfilment_info()}")
        print("  Supplier: ", end="")
        self.supplier.display_information()
    
    def to_dict(self) -> dict:
        return {"type": "digital", 
                "product_id": self._product_id, 
                "name": self.name, 
                "price": self._price, 
                "stock": self._stock, 
                "download size": self._download_size,
                "supplier": {
                    "supplier_id": self.supplier._supplier_id,
                    "name": self.supplier._name,
                    "contact_email": self.supplier._contact_email
                    }
                }