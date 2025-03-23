def tipCalculator():
    print("Welcome to the tip calculator.")
    totalBill = float(input("What was the total bill? $"))
    tipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))
    tip = totalBill * (tipPercentage / 100)
    totalBill += tip
    eachPerson = totalBill / people
    print(f"Each person should pay: ${round(eachPerson, 2)}")


tipCalculator()