print("Hello, World!")


list1 = ["Apple", "Cherry", "Orange"]

tuple1 = ("This", "is", "a", "tuple") #immutable elements cannot be changed, added, or removed

dict1 = {"name": "john", "age": 36}  #object

set1 = {"luigi", "mario", "peach"}


#list methods (like advanced array methods)
'''
append() -> adds to the end of a list
extend() -> joins two lists together
insert() -> (el, index) can sert insert an element at specified index
remove() -> removes the first occurence of a specified element
pop() -> remove and reutrn the element (can specify index or empty removes last index)
clear() -> removes all elements from the list

'''

def forloop():
    for x in list1:
        if x == "Apple":
            print("true")
        else:
            print("false")

# forloop()

def range1():
    for i in range(10):
        print(i)

# range1() 
# output is 0 -> 9  (not inclusive)

def rangelen1():
    for x in range(len(list1)):
        print(x)

rangelen1()
#output 0, 1, 2 


#lambda (ARROW FUNCTION)

x = lambda a : a + 10
print(x(5))

#func_name = lambda arg : func
#output 15


#lambda function is a small anonymous function
# a lambda function can take any number of arguments, but can only have on expression

x2 = lambda a, b : a * b
print(x2(5,6))

# Why use lambdas? ex anonymous lambda function inside another function

def myFunc(n):
    return lambda a : a * n

mydoubler = myFunc(2)
print(mydoubler(11)) # n == 2, a == 11

mytripler = myFunc(3)
print(mytripler(15)) # n == 3, a == 15