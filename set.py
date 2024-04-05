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


# Remove items from a Set
# you can use the remove() or discard() method

thisset.remove("apple")

# you can also use pop() but it removes a random item
# clear() will empty the set
# del thisset will delete the set complettely


for x in thisset:
    print(x)



# union() and update() methods join all tiems from both sets

# intersection() method keeps ONLY the duplicates

# difference() method keeps the items from the first set that are not in the other set(s)

# symmetric_difference() method keeps all items EXCEPT the duplicates




'''
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others



'''


fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")