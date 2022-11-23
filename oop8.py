# OOP Exercise 5: Define a property that must have the same value for every class instance (object)

class Vehicle:
    # Class attribute
    color1 = "White"
    color2 = "Black"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color1, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color2, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)