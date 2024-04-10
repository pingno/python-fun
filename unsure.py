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

