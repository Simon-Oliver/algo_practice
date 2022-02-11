class Player:
    def __init__(self, name, health=100):
        self.__name = name
        self.__health = health

    def take_damage(self,attack):
        self.__health -= attack.get_damage()
        print(f"{self.__name} took {attack.get_damage()} damage. Health is {self.__health}")

    def attack(self,target, attack):
        target.take_damage(attack)
        print(f"{self.__name} attacked {target.__name}. Health is {target.__health}")

class Attack:
    def __init__(self,name,dmg=0):
        self.__name = name
        self.__dmg = dmg

    def get_damage(self):
        return self.__dmg

    def set_damage(self,dmg):
        self.__dmg = dmg

fire = Attack("Fire",23)
water = Attack("Water",15)

bob = Player("Bob",100)
max = Player("Max",100)

bob.attack(max,fire)