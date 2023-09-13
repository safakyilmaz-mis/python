print("Welcome to love calculator.")
userName = input("Enter your name: ")
userName2 = input("Enter your love name: ")
userName = userName.lower()
userName2 = userName2.lower()

letters = ["t","r","u","e"]
letters2 = ["l","o","v","e"]

deneme = userName.count(letters[0])
deneme1 = userName.count(letters[1])

total = 0
total2 = 0
total3 = 0
total4 = 0

for i in letters:
    total += userName.count(i)
    total2 += userName2.count(i)

for a in letters2:
    total3 += userName.count(a)
    total4 += userName2.count(a)

percentage = total+total2
percentage1 = total3+total4

if percentage <= 1 or percentage >= 9:
    print(f"Your love score is %{percentage}{percentage1}. You go togetger like coke and mentos")
elif 4 <=percentage <= 5:
    print(f"Your love score is %{percentage}{percentage1}. You are alright together")
else:
    print(f"Your love score is %{percentage}{percentage1}.")

#I will update the codes soon it is a little bit mess I know :)
