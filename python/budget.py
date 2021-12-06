class Budget():
    def __init__(self, category, init_budget=None):
        self.ledger = []
        self.category = category
        if init_budget is not None:
            self.deposit(init_budget,"Initial deposit")
            self.budget = init_budget

    def deposit(self,amount, desc=""):
        self.ledger.append({"amount":amount,"description":desc})

    def get_balance(self):
        balance = 0
        for element in self.ledger:
            balance += element["amount"]
        return balance

    def check_funds(self, amount):
        return self.get_balance() + -abs(amount) >= 0

    def withdraw(self,amount,desc=""):
        if self.check_funds(amount):
            self.deposit(-abs(amount),desc)
            return True
        return False



    def transfer(self,amount,dest_budget):
        if self.withdraw(amount, 'Transfer to {}'.format(dest_budget.category)):
            dest_budget.deposit(amount,'Transfer from {}'.format(self.category))
            return True
        return False


food = Budget('Food',5000)
food.deposit(800,'Pay')
bills = Budget('Bills')

# print(food.get_balance())
# print(food.withdraw(50,"Shopping"))
food.transfer(1000,bills)
print("Food",food.ledger)
print("Bills",bills.ledger)