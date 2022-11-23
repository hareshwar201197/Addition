# OOP Exercise 2: Create a Vehicle 
# class without any variables and methods
"""
class vehical:
        pass"""

# OOP Exercise 3: Create a child class Bus that will inherit
# all of the variables and methods of the Vehicle class

class vehical:
    def __init__(self,name,max_speed,milage):
       self.name=name
       self.max_speed=max_speed
       self.milage=milage

class bus(vehical):
    pass
bus=vehical("Hari",120,20)
print("School_bus Name :" ,bus.name, "Max_peed of bus :" , bus.max_speed, "Milage of the bus :" , bus.milage)
 