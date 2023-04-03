print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? Rs "))
people = int(input("How many people to split the bill? "))
perc = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
final = (bill*(100+perc)/100)/people
print(f"Each person should pay: Rs {round(final,2)}")