"""
Exercise 2: ShoppingCart
Design ShoppingCart Class
Problem: Build a ShoppingCart class that manages items, supports a one-time discount code, and prevents modifications after checkout.

Requirements:

Private map/dictionary of items (item name to price)
Private discount code (can only be applied once)
Private isCheckedOut flag
addItem(name, price): adds an item, but only if the cart hasn't been checked out
applyDiscount(code): if the code is "SAVE10" and no discount has been applied yet, marks the discount as applied and stores it. Returns success/failure.
getTotal(): returns the sum of all prices, minus 10% if a discount was applied
checkout(): marks the cart as checked out if it has at least one item. After checkout, no items can be added and no discounts can be applied.
"""

class ShoppingCart:
    def __init__(self):
        self._cart: dict[str, float] = {}
        self._code_applied = False
        self._checked_out = False

    def add_item(self, name: str, price: float) -> None:
        if self._checked_out:
            print("Cannot modify a checked-out cart")
            return

        self._cart[name] = price
    
    def apply_discount(self, code: str) -> bool:
        if code == "SAVE10" and not self._code_applied and not self._checked_out:
            self._code_applied = True
            return True
        else:
            return False
        
    def get_total(self):
        price = sum(self._cart.values())
        if self._code_applied:
            return price * 0.9
        else:
            return price
    
    def checkout(self) -> None:
        if len(self._cart) > 0:
            self._checked_out = True


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 999.99)
    cart.add_item("Mouse", 29.99)

    print(f"Total: ${cart.get_total():.2f}")                     # 1029.98

    print(f"Discount: {str(cart.apply_discount('SAVE10')).lower()}")          # true
    print(f"Total: ${cart.get_total():.2f}")                     # 926.98

    print(f"Discount: {str(cart.apply_discount('SAVE10')).lower()}")          # false

    cart.checkout()
    cart.add_item("Keyboard", 79.99)  # Should be rejected
    print(f"Total: ${cart.get_total():.2f}")                     # 926.98