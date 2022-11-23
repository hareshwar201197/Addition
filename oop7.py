#Given:
# Create a Bus class that inherits from the Vehicle class.
# Give the capacity argument of Bus.seating_capacity() a default value of 50.

class vehicle:
    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage

    def seating_capacity(self,capacity):
        return f"The seating capacity of a {self.name} is {capacity} passenger"

class Bus(vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())


