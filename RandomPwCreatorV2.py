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
#e.g. 4 letter, 2 symbols, 2 number = g^2jk8&P

value = ["letters", "numbers", "symbols"]
len_password = nr_letters + nr_numbers + nr_symbols
password = ""
for l in range(1,len_password+1):
    random_value = random.choice(value)
    match random_value:
        case "letters":
            password += random.choice(letters)
        case "numbers":
            password += random.choice(numbers)
        case "symbols":
            password += random.choice(symbols)
            
print(password)
