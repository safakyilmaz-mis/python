#   This program will help you to calculate your BMI

H = float(input("Enter your height (enter meter e.g. 1.75): "))
#   getting information about height

W = int(input("Enter your weight: "))
#   getting information about weight

Total = W/(H*H)
#   calculation

Total = round(Total, 2)
#   we want to limit our result 2 digits after int number

print("Your BMI is: "+str(Total))
#   we are converting our float to string because, 
#   we can't print float and str at the same time
