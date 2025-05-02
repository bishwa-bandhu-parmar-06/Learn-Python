print("Which Year You want to Check That Is Leap year or Not?")

year = int(input("Enter Year You Want to Check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a Leap Year.")
        else:
            print(year,"Is not a Leap Year.")
    else:
        print(year, "is a Leap Year.")
else:
    print(year,"Is not a Leap Year.")