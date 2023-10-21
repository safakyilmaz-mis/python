import os

def plus(num1,num2):
    return num1+num2

def minus(num1,num2):
    return num1-num2

def mult(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

try_again = True
while try_again == True:
    
    operations = {"+":"plus",
            "-":"minus",
            "*":"multiplication",
            "/":"divide"}
    
    number1 = float(input("Enter first value: "))
    print("")
    for symbol in operations:
        print(f"for {operations[symbol]}: {symbol}")
    operation = input("Which operator do you want to choose? : ")
    number2 = float(input("\nEnter second value: "))

    answer = {"plus": plus(number1,number2),
            "minus":minus(number1,number2),
            "multiplication":mult(number1,number2),
            "divide":divide(number1,number2)}

    print(f"{number1} {operation} {number2}: {answer[operations[operation]]}")

    try_again_answer = input("Do you want to make another calculation? (yes/no): ")
    if try_again_answer == "no":
        try_again = False
    elif try_again_answer == "yes":
        try_again == True
        os.system("cls")
