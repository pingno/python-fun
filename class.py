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
    
    def __str__(self):
        return f"{self.name} weights about {self.weight} and has made {self.eggs} so far"



class Coder:
    def __init__(self, name, years_of_experience, languages, projects=None, additional_info=None):
        self.name = name
        self.years_of_experience = years_of_experience
        self.languages = languages
        self.projects = projects if projects else []
        self.additional_info = additional_info if additional_info else {}

    def add_project(self, project):
        self.projects.append(project)

    def add_additional_info(self, key, value):
        self.additional_info[key] = value

    def display_info(self):
        print("Coder Name:", self.name)
        print("Years of Experience:", self.years_of_experience)
        print("Languages:", ', '.join(self.languages))
        print("Projects:")
        for project in self.projects:
            print("- ", project)
        print("Additional Info:")
        for key, value in self.additional_info.items():
            print("- {}: {}".format(key, value))


# Example Usage:
if __name__ == "__main__":
    coder1 = Coder("John Doe", 5, ["Python", "Java", "JavaScript"], ["Project A", "Project B"])
    coder1.add_additional_info("Education", "Bachelor's in Computer Science")
    coder1.add_project("Project C")

    coder2 = Coder("Jane Smith", 3, ["C++", "Python"], additional_info={"Hobby": "Gaming"})

    coder1.display_info()
    print("\n")
    coder2.display_info()




class Pokemon:
    def __init__(self, name, lvl, type, health):
        self.name = name
        self.lvl = lvl
        self.type = type
        self.health = health

charmander = Pokemon("charmander", 3, "Fire", 80)
squirtle = Pokemon("Squirtle", 5, "Water", 80)