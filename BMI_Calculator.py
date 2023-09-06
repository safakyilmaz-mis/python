#   This program will help you to calculate your BMI

H = float(input("Enter your height (enter meter e.g. 1.75): "))
#   Getting information about height

W = float(input("Enter your weight: "))
#   Getting information about weight

#Total = round(W/(H*H),2)
Total = float(f"{W/(H*H):.2f}")
#   calculation
#   We want to limit our result to 2 digits after int number

print(f"Your BMI is: {Total}")
#   We are converting our float to string because, 
#   We can't print float and str at the same time

if Total < 18.5:
  print("You have underwaight")
elif Total < 25:
    print("You have normal weight")
elif Total < 30:
    print("You have overweight")
elif Total < 35:
    print("You have obese")
else:
    print("You are clinically obese")
    
#V2.0 adding new comments
