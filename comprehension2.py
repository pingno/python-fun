#I'm going to practice list comprehensions

colors = ["red", "white", "blue", "green", "yellow", "orange", "brown", "black", "purple"]
newlist = []

for x in colors: #for each item in colors
    if "a" in x: #if the letter a is in the specific color
        newlist.append(x)
        print(f"These colors {x} contain the letter a")


for x in colors:
    if len(x) > 4:
        newlist.append(x)
        print(f"the length of color {x} is longer than 4")


numList = [1, 2, 3, 4 ,5]

numList2 = [x*2 for x in numList if x % 2 == 0] #times 2
print(numList2)

numList3 = [x**2 for x in numList if x%2 == 0] #power of 2
print(numList3)

# numList4 = [x^2 for x in numList] # isn't a power of 2, it's a bitwise operator
# print(numList4)


numList5 = [x/2 for x in numList]
print(numList5) #0.5, 1.0, 2.0, 2.5


numList6 = [f"this num is {x}" for x in numList]
print(f"can you return a string interpolation in list comprehension?{x}" for x in numList6)
#not done properly returns <generator object <genexpr> at .....>



names = ["stewart", "bobby", "danny"]
name_dict = {name: len(name) for name in names}
print(names)



#creating a list of tuples
name_lengths = [(name, len(name)) for name in names]
print(f"list of tuples {name_lengths}")

#using a conditional expression
even_or_odd = ['even' if x % 2 == 0 else 'odd' for x in numList]

#creating a dictionary with list comprehensions