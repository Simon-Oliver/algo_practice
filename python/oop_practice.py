class Vehicle:
    def __init__(self, name, max_speed,milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

class Bus(Vehicle):
    pass

bus = Bus("School volvo",250,80)

print(bus.milage)