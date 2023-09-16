import random
print("Welcome to who will pay the bill gave v2")
names = input("Give me all names, seperated with ',' comma:\n")
listOfNames = names.split(",")
number = random.randrange(len(listOfNames))
print(f"{listOfNames[number]} will pay the bill today!")
