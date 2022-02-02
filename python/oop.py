class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations
        assert price >= 0, f"Price {price} can't be less than 0."
        assert quantity >= 0, f"Price {price} can't be less than 0."

        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_price = self.calculate_total_price()

        def set_price

    def calculate_total_price(self):
        return self.quantity * self.price

item1 = Item("Iphone", 2834,33)
print(item1.calculate_total_price())


