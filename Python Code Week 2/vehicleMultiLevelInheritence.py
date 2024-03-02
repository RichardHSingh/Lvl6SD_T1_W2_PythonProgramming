#============== MULTI_LEVEL INHERITANCE =====================

# vehicle class --> Base Class
class Vehicle:

    # method for starting engine
    def start_engine(self):
        print("Toot Toot chugga chugga big red car!\n")


# sub-class Car
class Car(Vehicle):

    #method for drive
    def drive(self):
        print("Before you take a ride you got to belt up quick\n")


# second sub-class
class ElectricCar(Car):
    
    #method charge battery
    def charge_battery(self):
        print("Tesla - MAXIMISE\n")


# instances
# instance for vehicle class
vehicle = Vehicle()
vehicle.start_engine()

# instance for car sub-class
car = Car()
car.start_engine()
car.drive()

# instance for electric car sub class
byd = ElectricCar()
byd.start_engine()
byd.drive()
byd.charge_battery()

