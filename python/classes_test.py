from datetime import datetime

class Person:
    def __init__(self,first, last, dbo):
        self.name = f"{first} {last}"
        self.dbo = dbo
        self.age = self.calculate_age()
        self.email = f"{first}.{last}@test.com"

    def calculate_age(self):
        today = datetime.today()
        born = datetime.strptime(self.dbo,"%d/%m/%Y")
        age = today.year - born.year
        return age

per1 = Person("Max","Muster", "23/06/1995")
print(per1.age)
print(per1.email)

class Employee(Person):
    def __init__(self,first, last, dbo, salary,is_active):
        self.salary = salary
        self.is_active = is_active
        self.email = f"{first}.{last}@company.com"
        super().__init__(first, last, dbo)

emp1 = Employee("Hans","Zimmer", "19/01/1960", 60000, True)
print(emp1.age)
print(emp1.email)
