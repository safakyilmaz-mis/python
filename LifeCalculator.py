# Average human life (years):80 years
# Average human life (months):80*12 months
# Average human life (weeks): 80*52 weeks
# Average human life (days): 80*365 days

age = int(input("How old are you?: "))
# Get the user's age
Year = 80 - age
# According to scientific results, human life is 80 years
# We are calculating how many years the user has

Year_Remaning =Year
Month_Remaning = Year *12
Week_Remaning = Year * 52 
Day_Remaning = Year * 365
# Basic math calculations
        
print(f"You have {Year_Remaning} years, {Month_Remaning} months, {Week_Remaning} weeks, {Day_Remaning} days left in your life")
# With the f print function you don't need to add + every time

# ---------------------------------------------------
# second and longer solution

# age = int(input("How old are you?: "))
# Year = 80
# Month = 80*12
# Week = 80*52
# Day=  80*365
        
# print(f"You have {Year-age} years, {Month-age*12} months, {Week-age*52} weeks, {Day-age*365} left in your life")
