#============== DEFAULT VALUES IN PARAMETER =====================

class Car:
     # constructor to have default values for model and make
    def __init__(self, make = "Tesla", model = "Model X", year = 69):

        # objects = make model and year
        self.make = make
        self.model = model
        self.year = year


# default car value call
defaultValue = Car()

print(defaultValue.make) # output = Tesla
print(defaultValue.model) #output = Model X
print(defaultValue.year) #output = 69


