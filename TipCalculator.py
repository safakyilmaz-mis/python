print("Welcome to the tip calculator.")

Bill = float(input("What was the total bill? $"))
# Get information on how much the bill

Tip = int(input("What percentage tip would you like to give? 10, 12, or 15? %"))
# How many percentages will pay tip

People = int(input("How many people to split the bill? "))
# Get how many people will divide the bill

Sum = (((Bill / 100)*Tip)+Bill)/People
# Calculations

print(f"Each person should pay: ${Sum:.2f}")
# Also possible with a round function
# Round(Sum, 2)
