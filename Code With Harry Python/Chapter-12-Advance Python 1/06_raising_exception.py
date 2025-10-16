a = int(input("Enter a Number : "))
b = int(input("Enter a Second Number : "))

if(b == 0):
    raise ZeroDivisionError("Hey our Program is not meant to divide numbers by Zero")
else:
    print(f"The Division a/b is {a/b}")