print("Buy The Ticket To Access the best Swing. ")

height = int(input("Enter The Height in Centimeter: "))

if height > 120:
    print("You Can Ride The Roller Coaster")
    age = int(input("Enter Your Age : "))
    if age > 18:
        print("You Have To pay $12.00")
    elif age < 18 and age > 12:
        print("You Have To pay $7.00")
    else:
        print("You Have To pay $5.00")
else:
    print("You Can Not Ride The Roller Coaster")