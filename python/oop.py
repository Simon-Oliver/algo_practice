class Item:
    # class attributes
    pay_rate = 0.5  # Setting an initial sales price at 50% off

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations
        assert price >= 0, f"Price {price} can't be less than 0."
        assert quantity >= 0, f"Price {price} can't be less than 0."

        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        return self.quantity * self.price

    def apply_discount(self):
        # Revering to self.pay_rate will make sure the instance pay rate
        # is used when applied specifically to an instance
        self.price = self.price * self.pay_rate

    def remove_discount(self):
        self.price = self.price / self.pay_rate


item1 = Item("Iphone", 100, 5)
print(item1.calculate_total_price())

print(item1.price)
# Adding a different sales rate to specific instance
item1.pay_rate = 0.8
item1.apply_discount()
print("Sales applied", item1.price)
item1.remove_discount()
print("Discount removed", item1.price)
