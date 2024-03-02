#============== PARAMETERISED CONSTRUCTOR =====================

# Oblong Class
class Rectangle:

    #constructor for rectangles length n width
    def __init__(self, length, width):
       
       # objects within constructor
       self.length = length
       self.width = width

# creating parameterised constructor
oblong = Rectangle(2,4)


print(f"This rectangle is {oblong.length} centimeters long and {oblong.width} centimeters wide")