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


# Classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
    
    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# __str__() function controls what should be returned when the class object is represented as a string
# if the __str__() function is not set, the string representation of the object is returned

print(p1) #outputs John(36)

p1.myfunc() # "Hello my name is John"

# Creating a child class
# to create a class that inherits the functionality from another, send the parent class as a parameter

class Student(Person):
    pass

timmy = Student("Mike", "Olsen")
timmy.myfunc()


#iterator vs iterable
# lists, tuples, dictionaries, and sets are all iterable objects
# they are iterable containers which you can get an iterator from

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit)) # apple
print(next(myit)) # banana
print(next(myit)) # cherry

for x in mytuple:
    print(x)

mystr = "banana"
for x in mystr:
    print(x) #iterate the characters of a string:





class Car:
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
    
    def car_year(self):
        print("the year for this car is " + self.year )

    def car_model(self):
        print("the model for this car is " + self.model)


    def car_make(self):
        print("the make for this car is " + self.make)

    def whatsmycar(self):
        print("This is the car you own " + self.model + self.make + self.year)




class Anime:
    def __init__(self, title, genre, episodes, rating):
        self.title = title
        self.genre = genre
        self.episodes = episodes
        self.rating = rating

    def __str__(self):
        return f"{self.title}({self.genre})"
    
    def anime_name(self):
        print("The anime's name is " + self.title)
    
    def anime_genre(self):
        print("The anime's genre is from " + self.genre)

    def anime_ep(self):
        print("There are " + self.episodes + "episodes")

    def rating(self):
        print("This anime has a rating of " + self.rating)

        