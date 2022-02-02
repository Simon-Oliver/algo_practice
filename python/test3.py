class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self,rad=5,color="green", on=False,speed=SLOW):
        self.on = on
        self.speed = speed
        self.rad = rad
        self.color = color

    def __str__(self):
        return f"{self.rad} {self.color} {self.on} {self.speed}"


fan1 = Fan()
print(fan1)