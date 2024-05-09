fruits = ["apple", "banana", "grape", "melon", "mango"]
newlist = []

for x in fruits: #for each item in fruits
    if "a" in x: #if the letter a is in the item
        newlist.append(x) #add to new list


newlist2 = [x for x in fruits if "a" in x]
    #return this for each item in fruits if "a" is in item