from item import Item
from phone import Phone

Item.init_from_csv()

phone1 = Phone('2017_Iphone', 500,5,1)
phone2 = Phone("2018_IPhone",800,6,1)

item1 = Item("My Item", 543)

print(item1.name)