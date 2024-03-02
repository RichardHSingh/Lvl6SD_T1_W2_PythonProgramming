#============== DATA STRUCTORS TUPLES =====================

# ---------EXERCISE 1---------

# creating tuple
coordinates = ()

# adding latitude and longitude values
x = list(coordinates)
x.append("69.9")
x.append("69.69")

# changing list back into tuple
coordinates = tuple(x)
print(coordinates)


# --------- TIP ---------
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# cannot append tuple as it is unmuteable - need to change to lsit first



# ---------EXERCISE 2 ---------

#  create tuple fruit
fruit = ()

# adding data into tuple but converting into list first
y = list(fruit)
y.append("Goose Berry")
y.append("Strawberry")
y.append("Rockmelon")

# changing list back into tuple
fruit = tuple(y)
print(fruit)

for element in fruit:
    if "banana" in element:
        print("banana is in your list")
        break
else:
    print("Banana is not in your list")
  

