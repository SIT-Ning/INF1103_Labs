from supply import Supplier
from physical import PhysicalProduct
from order import Order
import discount

def check(description, passed):
    if passed:
        print('PASS | ', description)
    else:
        print('FAIL | ', description)
        
supplier = Supplier("S001", "Tom", "tom@example.com")
laptop = PhysicalProduct("P001", "Laptop", 125.0, 10, 2.5, supplier)


check('NoDiscount keeps 100 as 100', discount.NoDiscount().apply(100) == 100)
check("10% off 250 gives 225", discount.PercentageDiscount(10).apply(250) == 225)
check("BulkDiscount(200, 20) on 250 gives 230", discount.BulkDiscount(200, 20).apply(250) == 230)
check("BulkDiscount(200, 20) on exactly 200 gives 180", discount.BulkDiscount(200, 20).apply(200) == 180)
check("BulkDiscount(200, 20) on 199 gives 199", discount.BulkDiscount(200, 20).apply(199) == 199)
check("StudentDiscount takes 5% off 100", discount.StudentDiscount().apply(100) == 95)


check("NoDiscount is a DiscountStrategy", isinstance(discount.NoDiscount(), discount.DiscountStrategy))
check("PercentageDiscount is a DiscountStrategy", isinstance(discount.PercentageDiscount(10), discount.DiscountStrategy))
check("BulkDiscount is a DiscountStrategy", isinstance(discount.BulkDiscount(200, 20), discount.DiscountStrategy))
check("StudentDiscount is a DiscountStrategy", isinstance(discount.StudentDiscount(), discount.DiscountStrategy))


order = Order("O001")
order.add_order(laptop, 2)
check("Order with no discount set totals 250", order.calculate_total() == 250)
order.set_discount(discount.BulkDiscount(200, 20))
check("Order with BulkDiscount totals 230", order.calculate_total() == 230)
order.set_discount(discount.PercentageDiscount(10))
check("set_discount replaces the old one: total is 225, not 207", order.calculate_total() == 225)


class HalfPrice(discount.DiscountStrategy):
    def apply(self, total):
        return total / 2

order.set_discount(HalfPrice())
check("new HalfPrice strategy works without editing Order", order.calculate_total() == 125)