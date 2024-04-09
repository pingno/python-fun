# Dictionaries ( like objects in JS ) 

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

print(thisdict["brand"])

print("the length of this dictionary is " + len(thisdict))

#Dictionary Items - Data Types
# The values in dictionary items can be of any data type:

mycarsbrand = thisdict["brand"]
mycarsmodel = thisdict.get("model")

keylist = thisdict.keys()


#LOOP DICTIONARIES

#print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)

#print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

#you can also use the values() method to return values of a dictionary
for x in thisdict.values():
 print(x)

 # you can use the keys() method to return the keys of a dictionary:
 for x in thisdict.keys():
    print(x)


#loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
   print(x, y)


#copy dictionaries
seconddict = thisdict.copy()


'''
Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

'''