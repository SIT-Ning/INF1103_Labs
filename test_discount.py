import unittest
import inspect

import order as order_module
from discount import (DiscountStrategy, NoDiscount, PercentageDiscount,
                      BulkDiscount, StudentDiscount)
from order import Order
from physical import PhysicalProduct
from supply import Supplier

def make_order(discount=None) -> Order:
    supplier = Supplier("S001", "Tom", "tom@example.com")
    product = PhysicalProduct("P001", "Laptop", 125.0, 10, 2.5, supplier)
    order = Order("O001", discount) if discount else Order("O001")
    order.add_order(product, 2)
    return order

class TestDiscountStrategies(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(NoDiscount().apply(100), 100)

    def test_percentage_discount(self):
        self.assertAlmostEqual(PercentageDiscount(10).apply(250), 225)

    def test_bulk_discount_at_and_above_threshold(self):
        self.assertEqual(BulkDiscount(200, 20).apply(250), 230)
        self.assertEqual(BulkDiscount(200, 20).apply(200), 180)

    def test_bulk_discount_below_threshold(self):
        self.assertEqual(BulkDiscount(200, 20).apply(199), 199)

    def test_student_discount_is_five_percent(self):
        self.assertAlmostEqual(StudentDiscount().apply(100), 95)

    def test_strategies_inherit_from_base(self):
        for cls in (NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount):
            self.assertTrue(issubclass(cls, DiscountStrategy))

    def test_invalid_percentage_rejected(self):
        with self.assertRaises(ValueError):
            PercentageDiscount(150)


class TestOrderUsesStrategy(unittest.TestCase):
    def test_default_is_no_discount(self):
        self.assertEqual(make_order().calculate_total(), 250)

    def test_bulk_discount_on_order(self):
        self.assertEqual(make_order(BulkDiscount(200, 20)).calculate_total(), 230)

    def test_set_discount_changes_strategy(self):
        order = make_order(BulkDiscount(200, 20))
        order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(order.calculate_total(), 225)

    def test_new_strategy_needs_no_change_to_order(self):
        class HalfPrice(DiscountStrategy):
            def apply(self, total: float) -> float:
                return total / 2

        self.assertEqual(make_order(HalfPrice()).calculate_total(), 125)

    def test_order_has_no_discount_if_elif_logic(self):
        source = inspect.getsource(order_module.Order)
        for word in ("percentage", "bulk", "student", "elif"):
            self.assertNotIn(word, source.lower())


if __name__ == "__main__":
    unittest.main()
