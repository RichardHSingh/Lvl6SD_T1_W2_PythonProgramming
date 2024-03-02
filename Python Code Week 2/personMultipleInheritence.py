#============== DERIVED CLASS =====================

# Person class --> Base 1
class Person: 

    # attributes
    def __init__ (self, name, age):
        self.name = name
        self.age = age



# Skill class --> Base 2
class Skill:

    # attributes
    def __init__(self, programming_skill, communication_skill):
        self.programming_skill = programming_skill
        self.communication_skill = communication_skill


# Employee class --> Derived class
class Employee(Person, Skill):

    def __init__(self, name, age, programming_skill, communication_skill):
        
    #calling attributes from both parents hard to see but there is a dot after parents class
        Person. __init__(self, name, age)
        Skill. __init__(self, programming_skill, communication_skill)

# values to derived class
employee = Employee("John", 20, "Intermediate", "Exceptional")

# printing values assigned after inheriting from parents
print(f"Name is {employee.name} and I am {employee.age} years old.\n")
print(f"My programming skills are at {employee.programming_skill} level and my communition skills are {employee.communication_skill}.")



