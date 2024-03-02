#============== DATA STRUCTORS SETS =====================

# ---------EXERCISE 1 ---------

#creating set function
def common_element(set1,set2):

    #setting the sets to an empty shell to add elements into
    x = set(set1) 
    y = set(set2)

    #use update for multiple elements and add for single element
    x.update(["Blue", "Red", "Green", "Black", "Pink"])
    y.update(["Pink", "Orange", "Red", "Yellow", "Silver"])

    #insection_update finds the common elements in both sets
    x.intersection_update(y)

    #printing the output
    print(f"{x} are the comment elements")


common_element(set(), set())




# ---------EXERCISE 2 ---------

#creating function to remove sets
def remove_duplicates(set_list):

    # setting set to remove double-ups
    duplicate_set = set(set_list)

# set needs to be converted into list to remove double-ups but more importantly, keep items in the same index
    set_list = list(duplicate_set)

    return duplicate_set

#creating duplicates for program
duplicate_list = [10, 10, 20, 20, 30, 30, 40, 50, 60, 70]

#resutl will look for (duplicate_lsit) in function
resulting_list = remove_duplicates(duplicate_list)

print(f"\nMy original list was {duplicate_list}")
print(f"\nAfter removing duplicates, my list now looks like {resulting_list}")




















