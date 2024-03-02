##============== DATA STRUCTURE DICTIONARY =====================

#---------EXERCISE 1 ---------

# creating library catalog
library_catalog = {}

# adding elements into the dictionary [key : value]
library_catalog.update({"Book" : "Harry Pothead",
                        "Title" : "Chamberof Secret"})


print(library_catalog)


# ---------TIP ---------
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)



# ---------EXERCISE 2 ---------

# creating function doing same as above but iwht more precision 

def dictionary_list(input_word):
    dictionary_length = {}
    #looping though the list and count then returning the count
    for word in input_word:
        dictionary_length[word] = len(word)
    return dictionary_length


mywords = ["Naruto", "One Piece", "Bleach"]
result = dictionary_list(mywords)
print(result)

# my words in the hard coded word in the list
# results looks for mywords under the function name = list of words
# which then returns the results

