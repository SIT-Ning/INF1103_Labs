import unittest

from digital import DigitalProduct
from orderline import OrderLine
from physical import PhysicalProduct
from product_factory import ProductFactory
from supply import Supplier


class TestProductFactory(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S001", "Tom", "tom@example.com")

    def test_creates_physical_product(self):
        p = ProductFactory.create("physical", "P1", "Lamp", 25.0, 10, self.supplier, 2.0)
        self.assertIsInstance(p, PhysicalProduct)

    def test_creates_digital_product(self):
        p = ProductFactory.create("digital", "D1", "Editor", 49.9, 100, self.supplier, 500)
        self.assertIsInstance(p, DigitalProduct)

    def test_unknown_type_raises_clear_error(self):
        with self.assertRaises(ValueError) as ctx:
            ProductFactory.create("service", "S1", "Install", 30.0, 5, self.supplier)
        self.assertIn("Unknown product type: service", str(ctx.exception))


class TestValidation(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S001", "Tom", "tom@example.com")

    def test_price_must_be_positive(self):
        for bad in (0, -1):
            with self.assertRaises(ValueError):
                ProductFactory.create("physical", "P1", "Lamp", bad, 1, self.supplier)

    def test_digital_product_also_enforces_price_rule(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("digital", "D1", "Editor", 0, 1, self.supplier)

    def test_stock_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P1", "Lamp", 10.0, -1, self.supplier)

    def test_zero_stock_allowed(self):
        ProductFactory.create("physical", "P1", "Lamp", 10.0, 0, self.supplier)

    def test_order_line_quantity_must_be_positive(self):
        product = ProductFactory.create("physical", "P1", "Lamp", 10.0, 5, self.supplier)
        for bad in (0, -3):
            with self.assertRaises(ValueError):
                OrderLine(product, bad)


if __name__ == "__main__":
    unittest.main()