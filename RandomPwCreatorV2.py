#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomized:
#e.g. 4 letters, 2 symbols, 2 numbers = g^2jk8&P

value = ["letters", "numbers", "symbols"]
len_password = nr_letters + nr_numbers + nr_symbols
password = []

l = 0
for l in range(1,len_password+1):
    if nr_letters != 0:
        password += random.choice(letters)
        nr_letters -= 1
    elif nr_numbers != 0:
        password += random.choice(numbers)
        nr_numbers -= 1
    elif nr_symbols != 0:
        password += random.choice(symbols)
        nr_symbols -= 1

random.shuffle(password) #Randomize the order of characters within each category 

passText = ""
for x in range(len(password)):
    passText += password[x]
print(passText)

#or for loop can also written like that
#[print(totalPass) for x in password]
