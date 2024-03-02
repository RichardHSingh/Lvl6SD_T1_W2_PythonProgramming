#============== CAR CLASS WITH OBJECTS =====================

# CLASS FOR CAR
class Car:

     # constructor to be able to create car objects of make, model and year
    def __init__(self, make, model, year):

        # objects = make model and year
        self.make = make
        self.model = model
        self.year = year


# printing car attributes
myCar = Car("Mazda", "RX-7", 2003)

print(myCar.make) # output should be nissan
print(myCar.model) #output should be Caravan NV350
print(myCar.year) #output should be 2013


# two ways of writing this

myCar = Car(make = "Ford", model = "Mustang", year = 1969)

# Print the attributes of the car
print("Make:", myCar.make)
print("Model:", myCar.model)
print("Year:", myCar.year)
print(f"Make of your car is {myCar.model} and the model is {myCar.model} which was made in year {myCar.year}")


# Creating three different Car objects with different values
firstCar = Car(make = "Toyota", model = "Corolla", year = 2007)
secondCar = Car(make = "Ford", model = "Mustang", year = 1969)
thirdCar = Car(make = "Mistsubishi", model = "VR-4", year = 2000)

print(f"\n\n• My first car was a {firstCar.make} {firstCar.model} which was made is {firstCar.year}")
print(f"• The one vehicle I had always wanted is a {secondCar.year} {secondCar.make} {secondCar.model}")
print(f"• Have always been fond of {thirdCar.make} {thirdCar.model}, mostly from the year {thirdCar.year}")

