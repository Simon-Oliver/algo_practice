class Vehicle:
    def __init__(self, name, max_speed,milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

class Bus(Vehicle):
    def __init__(self, name,max_speed,milage, capacity):
        super().__init__(name,max_speed,milage)
        self.__capacity = capacity
    def get_capacity(self):
        return self.__capacity

bus = Bus("School volvo",250,80,45)

print(bus.get_capacity())
