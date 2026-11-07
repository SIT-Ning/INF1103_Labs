class Supplier:
   def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
       self._supplier_id = supplier_id
       self._name = name
       self._contact_email = contact_email
    
   @classmethod
   def supply_input(cls) -> Supplier:
       print("\nAdd supplier details")
       s_id = input("Supplier ID: ")
       s_name = input("Name: ")
       s_email = input("Contact email: ")
       return Supplier(s_id, s_name, s_email)

   def display_information(self) -> None:
       print(f"| ID: {self._supplier_id} | Name: {self._name} | Contact email: {self._contact_email}")
       