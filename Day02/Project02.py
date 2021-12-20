print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
perc = input("What percentage tip would you like to give? 10, 12, or 15? 12")
split = input("How many people to split the bill? ")

total = float(total)
perc = int(perc)
split = int(split)

perc = perc/100
total_tip =  total * perc
total = total + total_tip
total = total / split
print("Each person should pay: ${:.2f}".format(total))
