print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? $"))
tip_inp=int(input("How much tip would you like to give? 10, 12, or 15? "))
splits=int(input("How many people to split the bill? "))
tip=tip_inp/100
bill_tip=round((total_bill/splits)*(1+tip),2)
print(f"Each person should pay: ${bill_tip}")