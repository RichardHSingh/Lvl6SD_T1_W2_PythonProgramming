#============== DATA STRUCTURE LISTS =====================

# ---------EXERCISE 1 ---------


#creating shopping list
shopping_list = []

# append = adding items to the list
shopping_list.append ("apple")
shopping_list.append ("banana")
shopping_list.append ("orange")

# printing the list
print(shopping_list)


# --------- TIP ---------
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]

# thislist.extend(tropical)

# print(thislist)
# combines the lists



# ---------EXERCISE 2 ---------

# extending the list

# creating 2nd list
shopping_list1 = []
shopping_list1.append("grapes")

# as name says --> removes " " from list
shopping_list.remove("banana")

# displaying both lists into 1 --> combines the list using extend keyword
shopping_list.extend(shopping_list1)
print(shopping_list)
