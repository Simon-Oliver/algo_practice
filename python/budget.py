import math


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

    def center_padding(self,total_len,char,str):
        front = char * (math.floor((total_len-len(str))/2))
        back = char * (math.ceil((total_len-len(str))/2))
        return f'{front}{str}{back}'

    def padding_between(self,left,right=None):
        if right is not None:
            return f"{left.ljust(23)[:23]}{str(format(right,'.2f')).rjust(7)[:7]}"
        return f"{left.ljust(30)[:30]}"

    def __str__(self):
        new_str = self.center_padding(30,"*",self.category) + "\n"
        for e in self.ledger:
            new_str += self.padding_between(e["description"],e["amount"]) + "\n"
        new_str += self.padding_between(f'Total: {self.get_balance():.2f}')
        return new_str
        

food = Budget('Food',5000.548)
food.deposit(800,'Pay')
bills = Budget('Bills')

# print(food.get_balance())
# print(food.withdraw(50,"Shopping"))
food.transfer(1000,bills)
print("Food",food.ledger)
print("Bills",bills.ledger)
print(food)