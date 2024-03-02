#============== INHERITANCE-SINGLE =====================


# animals class
class Animals:
    # make sound method
    def make_sound(self):
        print("Sound")

# sub class dog 
class Inu:
    # override make sound method
    def make_sound(self):
        print("\nWoof Woof")


# Animal and general sound made
animals = Animals()
animals.make_sound()

# creating instance for doggy and its sound
dog = Inu()
dog.make_sound()

#"instance" refers to an object created from a class.
# single heritence as the dog is inheriting make sound from animals