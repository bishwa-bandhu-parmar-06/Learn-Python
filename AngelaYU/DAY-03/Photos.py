print("Buy The Ticket To Access the best Swing. ")

height = int(input("Enter The Height in Centimeter: "))

if height > 120:
    print("You Can Ride The Roller Coaster")
    age = int(input("Enter Your Age : "))
    if age > 18:
        bill = 12
        print("You Have To pay $12.00")
    elif age < 18 and age > 12:
        bill = 7
        print("You Have To pay $7.00")
    else:
        bill = 5
        print("You Have To pay $5.00")
    wants_Photo = input("You Want to Take Photo? Enter Y for Yes, N for No : ")
    if wants_Photo == "Y":
        bill += 3
        # print(f"Your Final Bill is ${bill}")
    print(f"Your Final Bill is ${bill}")   
else:
    print("You Can Not Ride The Roller Coaster")