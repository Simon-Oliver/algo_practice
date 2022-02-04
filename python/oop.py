import csv

class Item:
    # class attributes
    pay_rate = 0.5  # Setting an initial sales price at 50% off
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations
        assert price >= 0, f"Price {price} can't be less than 0."
        assert quantity >= 0, f"Price {price} can't be less than 0."

        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_price = self.calculate_total_price()

        # Add new items to list
        Item.all.append(self)

    def calculate_total_price(self):
        return self.quantity * self.price

    def apply_discount(self):
        # Revering to self.pay_rate will make sure the instance pay rate
        # is used when applied specifically to an instance
        self.price = self.price * self.pay_rate

    def remove_discount(self):
        self.price = self.price / self.pay_rate

    def __repr__(self):
        return f'Item("{self.name}",{self.price},{self.quantity})'

    # Class Method
    @classmethod
    def init_from_csv(cls):
        with open('items.csv',"r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                Item(item['name'],float(item['price']),int(item['quantity']))

Item.init_from_csv()
print(Item.all)
