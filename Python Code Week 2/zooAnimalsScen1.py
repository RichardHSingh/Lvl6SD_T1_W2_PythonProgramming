#============== SINGLE INHERITANCE =====================

# generic info about animals
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"\n{self.name} makes a generic sound")


# info about mammals such as fur color and species
class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def give_birth(self):
        print(f"\n{self.name} is giving birth")


# bird info and info if able to fly or not and color of feather
class Bird(Animal):
    def __init__(self, name, species, feather_color):
        super().__init__(name, species)
        self.feather_color = feather_color

    def fly(self):
        print(f"\n{self.name} is flying")


class Marine(Animal):
    # Attributes
    def __init__(self, name, species, diet_type):
        # data from parent animal
        super().__init__(name, species)
        self.diet_type = diet_type

    # marine method
    def diet(self):
        print(f"\n{self.name}'s diet is {self.diet_type} ")

# Instances
animal = Animal("Generic", "Unknown")
animal.make_sound()

hinata = Mammal("Hinata", "Hyuga", "Brown")
hinata.give_birth()

don = Bird("Don the bird", "DoDo", "Black")
don.fly()

babyShark = Marine("Carnivorous", "Shark", "Carnivorous")
babyShark.diet()
