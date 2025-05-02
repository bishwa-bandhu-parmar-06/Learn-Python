print("Welcome to the Tip Calculator.")

bill = float(input("What was the Total bill? : "))

tip = int(input("What percentage Tip would you like to give ? 10%, 12%, or 15% : "))

person = int(input("How many person to split the bill ? : "))

percent = bill * (tip / 100)
total_bill = bill + percent
numberOfPerson = round(total_bill / person, 2)
print(f"each person Should Pay : {numberOfPerson} rupees.")