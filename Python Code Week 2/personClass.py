#============== PERSON CLASS W' CONSTRUCTOR N' DESTRUCTOR =====================

class Person:
    def __init__(self, name, age):

        # persons attribute
        self.name = name
        self.age = age
        

    def __del__(self):
        # Destructor method that prints a message when a name and age object is deleted
        print(f"\n{self.name} {self.age} has been deleted.")
            


person1 = Person("Jake Hodson-Tomokino", 18)

print(f"\nKia Ora bro, mera num hae {person1.name} aur hum {person1.age} sul ke hae")

# del is keyword in pyton to delete something
del person1







