"""
Exercise 1: Discount Calculator
Design Discount Calculator Class
Problem: Build a pricing system where an OrderProcessor applies discounts polymorphically. 
Different discount types share a common base class with shared formatting logic, but each one calculates the discounted price differently. 
The processor works with any discount through the abstract Discount type.

Requirements:

Abstract Discount class with a label field (protected), an abstract apply(price) method that returns the discounted price, and a concrete describe(originalPrice) method that prints "label: $originalPrice -> $discountedPrice".
PercentageDiscount: takes a percentage (e.g., 20 means 20% off). Label is "20.0% off". Returns price * (1 - percentage/100).
FlatDiscount: takes a fixed amount off. Label is "$15.0 off". Returns price - amount (minimum 0).
BuyOneGetOneFree: halves the price. Label is "Buy 1 Get 1 Free". Returns price / 2.
OrderProcessor class with a processOrder(itemName, price, discount) method that prints the item name and calls describe() on the discount.
"""

from abc import ABC, abstractmethod

class Discount(ABC):
    def __init__(self, label: str) -> None:
        self._label = label

    @abstractmethod
    def apply(self, price: float) -> float:
        pass

    def describe(self, original_price: float) -> None:
        discounted_price = self.apply(original_price)
        print(f"{self._label}: ${original_price} -> ${discounted_price}")


class PercentageDiscount(Discount):
    def __init__(self, percentage: float) -> None:
        super().__init__(f"{percentage}% off")
        self._percentage = percentage
    
    def apply(self, price: float) -> float:
        return price * (1 - self._percentage / 100)


class FlatDiscount(Discount):
    def __init__(self, amount: float) -> None:
        super().__init__(f"${amount} off")
        self._amount = amount

    def apply(self, price: float) -> float:
        return max(0, price - self._amount)


class BuyOneGetOneFree(Discount):
    def __init__(self) -> None:
        super().__init__("Buy 1 Get 1 Free")

    def apply(self, price: float) -> float:
        return price / 2


class OrderProcessor:
    def process_order(self, item_name: str, price: float, discount: Discount) -> None:
        print(item_name)
        discount.describe(price)