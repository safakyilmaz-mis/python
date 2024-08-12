import os
from art2 import logo

print(logo+"\nWelcome to the secret auction program.")
name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
next_person = input("Are there any other bidders? Type 'yes' or 'no': ")

auction = [{
    "name": name,
    "bid": bid,
},]
while next_person == "yes":
    os.system('cls')
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction += [{"name": name,
               "bid": bid},]
    next_person = input("Are there any other bidders? Type 'yes' or 'no': ")

if next_person == "no":
    for i in range(len(auction)):
        if auction[i]["bid"] > auction[0]["bid"]:
            auction[0]["name"] = auction[i]["name"]
            auction[0]["bid"] = auction[i]["bid"]
    print(f"The winner is {auction[0]["name"]} ${auction[0]["bid"]}")

# print(auction)
