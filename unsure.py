oneslash = 5 / 2
print(oneslash)

twoslash = 10 // 2
print(twoslash)

# single slash will return floating point 

# if you use a single slash for a division problem that's decimal
# it will NOT round up and exclude the decimal

fruits = ["banana", "apple", "cherry", "peach"]

for x in range(len(fruits)):
    print(x)

#this will not print each fruit
# len of fruits is 4, range will go from 0 - 3

for x in fruits:
    print(x)
# this will print each fruit


# LIST COMPREHENSION
        # [(returns this) (loop) (conditional)]
newlist = [x for x in fruits if"a" in x]
print(newlist)

newlist2 = ["hi" for x in fruits if "a" in x]
print(newlist2)


#THE SYNTAX FOR LIST COMPREHENSION
# newlist = [expression for item in iterable if condition == True]


# initializing multiple variables

x, y, z = 1, 2, 3
print(x, y, z)



newlist = [x for x in fruits if x != "apple"]

newlist = [x for x in range(10)]

newlist = [x for x in range(10) if x < 5]

newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits]



thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

numlist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#make a copy

copythislist = thislist.copy()
copynumlist = list(numlist)
print(copynumlist)


'''

append() - adds an element at the end of the list
clear() - removes all the elments from the list
copy() - return sa copy of the list
count() - returns the number of elements with the specified value
extend() - add the elements of a list (or any iterable), to the end of the current list
index() - returns the index of the first element with the specified value
insert() - adds an element at the specified position
pop() - removes the element at the specified position
remove() - removes the item with the specified value
reverse() - reverse the order of the list
sort() - sorts the list

'''