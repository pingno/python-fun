class Dog: 
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.is_hungry = False
        self.is_sleeping = False
    
    def bark(self):
        return "Woof"
    
    def eat(self):
        self.is_hungry = False
        return f"{self.name} is eating."
    
    def sleep(self):
        self.is_sleeping = True
        return f"{self.name} is sleeping."
    
    def wake_up(self):
        self.is_sleeping = False
        return f"{self.name} woke up."
    
    def hunger_status(self):
        if self.is_hungry:
            return f"{self.name} is hungry."
        else:
            return f"{self.name} is not hungry."
        
    def __str__(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}."
    

dog1 = Dog("Buddy", "Australian Shepherd", 5)
dog2 = Dog("Sammy", "Border Collie", 2)

print(dog1)



class Cat:
    def __init__(self, breed, name, age, weight):
        self.breed = breed
        self.name = name
        self.age = age
        self.is_hungry = False
        self.is_fat = False

    def meow(self):
        return "Meow!"
    
    def eat(self):
        if self.is_hungry:
            return f"{self.name} is hungry"
        else:
            return f"{self.name} is not hungry"
        

class Chicken:
    def __init__(self, name, eggs, weight):
        self.name = name
        self.eggs = eggs
        self.weight = weight

    def chirp(self):
        return "Chirp Chirp!"
    
    def numEggs(self):
        return f"{self.name} has laid {self.eggs}"