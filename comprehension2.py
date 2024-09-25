#I'm going to practice list comprehensions

colors = ["red", "white", "blue", "green", "yellow", "orange", "brown", "black", "purple"]
newlist = []

for x in colors: #for each item in colors
    if "a" in x: #if the letter a is in the specific color
        newlist.append(x)
        print(f"These colors {x} contain the letter a")



