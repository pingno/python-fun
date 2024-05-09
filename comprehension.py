fruits = ["apple", "banana", "grape", "melon", "mango"]
newlist = []

for x in fruits: #for each item in fruits
    if "a" in x: #if the letter a is in the item
        newlist.append(x) #add to new list
        print(newlist)


newlist2 = [x for x in fruits if "a" in x]
    #return this for each item in fruits if "a" is in item

print(newlist2)


numlist = [1, 2, 3, 4, 5]

newnums = [x*3 for x in numlist if x % 2 == 0]
print(newnums)

#squaring numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)

#filtering with condition and applying operation:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_and_squared = [x**2 for x in numbers if x % 2 == 0]
print(filtered_and_squared)

#nested list comprehension (Flattening a list of lists):
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list)

#creating a lsit of tuples
names = ['Alice', 'Bob', 'Charlie']
name_lengths = [(name, len(name)) for name in names]
print(name_lengths)

#using a conditional epression
numbers = [1, 2, 3, 4, 5]
even_or_odd = ['even' if x % 2 == 0 else 'odd' for x in numbers]
print(even_or_odd)

#creating a dictionary with list comprehensions
names = ['Alice', 'Bob', 'Charlie']
name_dict = {name: len(name) for name in names}
print(name_dict)