# Leap year calculator
print("Welcome to leap year calculator.")
Year = int(input("Enter year to learn this is leap year or not: "))
        
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
# Every 4 year leap year
# Every 100 years, not leap year even if it can be divided by 4
# Every 400-year leap year whenever it is

    print("This is a leap year")
else:
    print("This is not a leap year")
    
# ------------------ or -----------------------
# if Year % 400 == 0:
#     if Year % 4 == 0:
#         print("This is a leap year")
# elif Year % 100 == 0:
#     print("This is not a leap year")
# else:
#     if Year % 4 == 0:
#         print("This is a leap year")
#     else:
#         print("This is not a leap year")
