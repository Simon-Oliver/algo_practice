import csv

class Item:
    # class attributes
    pay_rate = 0.5  # Setting an initial sales price at 50% off
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations
        assert price >= 0, f"Price {price} can't be less than 0."
        assert quantity >= 0, f"Price {price} can't be less than 0."
        # Double underscore makes the attribute private, so it can't be changed after instantiating the instance.
        self.__name = name
        self.__price = price
        self.quantity = quantity
        self.total_price = self.calculate_total_price()

        # Add new items to list
        Item.all.append(self)

    # This line allows us to return name when calling instance.name but prevents from reassigning
    @property
    # property decorator = read only attribute
    # basically a getter
    def name(self):
        return self.__name

    # Create a setter
    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if value < 0:
            raise Exception("Value needs to be 0 or larger.")
        else:
            self.__price = value

    def calculate_total_price(self):
        return self.quantity * self.price

    def apply_discount(self):
        # Revering to self.pay_rate will make sure the instance pay rate
        # is used when applied specifically to an instance
        self.__price = self.__price * self.pay_rate

    def remove_discount(self):
        self.__price = self.__price / self.pay_rate

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}",{self.__price},{self.quantity})'

    @staticmethod
    def check_if_is_integer(num):
        if isinstance(num, float):
            # This is needed to rule out numbers such as 5.0 to represent as integer
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Class Method
    @classmethod
    def init_from_csv(cls):
        with open('items.csv', "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                Item(item['name'], float(item['price']), int(item['quantity']))