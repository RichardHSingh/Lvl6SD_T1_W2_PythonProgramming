#============== DESTRUCTOR TO DELETE VARIABLE =====================

# creating a destructor
class Car:
    
    #constructor same as that of class and constructor code
    def __init__(self, make, model):
        # Constructor method to initialize the Car object with make and model
        self.make = make
        self.model = model


    # creating a destructor method
    def __del__(self):

        # Destructor method that prints a message when a Car object is deleted
        print(f"{self.make} {self.model} has been deleted.")

# Creating two Car objects
car1 = Car("Holden", "Clubsport")
car2 = Car("Honda", "CIVIC SIR")

# Deleting one of the Car objects
del car1  # This will trigger the __del__ method for car1

# del is a key word that deletes objects


