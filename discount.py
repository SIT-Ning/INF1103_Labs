from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass
    
class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total
    
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float) -> None:
        if not 0 <= percentage <= 100:
            raise ValueError("Percentage must be between 0 and 100")
        self._percentage = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self._percentage / 100)
    
class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float) -> None:
        if threshold < 0 or amount < 0:
            raise ValueError("Threshold cannot be negative")
        self._threshold = threshold
        self._amount = amount
        
    def apply(self, total: float) -> float:
        return total - self._amount if total >= self._threshold else total
    

class StudentDiscount(PercentageDiscount):
    def __init__(self) -> None:
        super().__init__(5)
        