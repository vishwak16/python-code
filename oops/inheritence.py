class Vehicle:
    def generalusage(self):
        print("used for transportaion")
class car(Vehicle):
    def __init__(self):
        print("i'm a car")
        self.wheels=4
        self.hasroof= True
    def specifications(self):
        print("specifications : can transport upto 4 people")

class Bike(Vehicle):
    def __init__(self):
        self.wheels=2
        self.hasroof=True
    def specifications(self):
        print("specifications : can transport upto 2 people")
c= car()
c.generalusage()
c.specifications()