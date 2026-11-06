class Supplier:
   def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
       self._supplier_id = supplier_id
       self._name = name
       self._contact_email = contact_email

   def display_information(self) -> None:
       print(f"ID: {self._supplier_id} | Name: {self._name} | Contact email: {self._contact_email}")