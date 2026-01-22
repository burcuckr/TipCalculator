print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $\n"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))
tip_as_percent = tip / 100
tot_tip = bill * tip_as_percent
tot_bill = bill + tot_tip
bill_per_person = tot_bill / people
rounded = round(bill_per_person, 2)
print(f"Each person should pay {rounded}$ ")