#============== CHECKING SIZE OF RECTANGLE =====================

# Oblong Class
class Rectangle:

    #constructor for rectangles length n width
    def __init__(self, length = 1, width = 1): # these lengths are default values unless changed later in code
       
       #objects for the constructor --> x and y axis
       self.length = length
       self.width = width

# creating parameterised constructor
oblong = Rectangle(2,4)

defaultOblong = Rectangle()# return should be the default value not the parameterised 

print(f"This rectangle is {oblong.length} centimeters long and {oblong.width} centimeters wide")
# tesing both output with repective values/parameters
print(f"\nThis default rectangle length is {defaultOblong.length} centimeters and width is {defaultOblong.width} centimeters.")
