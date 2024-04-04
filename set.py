#Sets are used to store multiple items in a single variable

# Set is one of 4 built-in data types in Python used to store collections of data

# UNORDERED, UNCHANGEABLE, and UNINDEXED
# They do not allow duplicate values
# They do not have a defined order

thisisset = {"apple", "banana", "cherry"}
print(thisisset)

for x in thisisset:
    print(x)

#check if "banana" is present in the set:
    print("banana" in thisisset) #true

#check if "banana" is NOT present in the set:
    print("banana" not in thisisset)

# Add an item to a set, using the add() method:
    thisisset.add("orange")
    print(thisisset)


#Add Sets
    # to add items from another set into the current set, use the update() method.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

print(thisset)

# Can also add any iterable object such as tuples, lists, dictionairies etc.

