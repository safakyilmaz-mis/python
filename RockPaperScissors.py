import random
print("Welcome to rock paper scissors game.\n")
user = int(input("What do you choose? (Please enter number: 1,2,3) \n1-Rock \n2-Paper\n3-Scissors\n\n"))
pc = random.randint(1,3)
if user == 1:
    if pc == 1:
        print("You slected Rock and PC selected Rock, Draw.")
    elif pc == 2:
        print("You slected Rock and PC selected Paper, PC won!")
    elif pc == 3:
        print("You slected Rock and PC selected Scissors, You won!")
        
elif user == 2:
    if pc == 1:
        print("You selected Paper and PC selected Rock, You won!")
    if pc == 2:
        print("You selected Paper and PC selected Paper, Draw.")
    elif pc == 3:
        print("You selected Paper and PC selected Scissors, PC won!")
        
elif user == 3:
    if pc == 1:
        print("You selected Scissors and PC selected Rock, PC won!")
    if pc == 2:
        print("You selected Scissors and PC selected Paper, You won!")
    elif pc == 3:
        print("You selected Scissors and PC selected Scissors, Draw.")
