#============== CLASSES AND OBJECTS =====================

# class named Car
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

text = '123'
print("\x1B[3m 123 \x1B[0m")
# anything in between --> \x1B[3m 123   x1B[0m will be displayed in ITALICS



   







