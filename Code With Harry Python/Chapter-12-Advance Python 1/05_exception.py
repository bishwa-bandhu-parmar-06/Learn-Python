try:
    a =int(input("Hey, Enter a Number: "))
    print(a)
except ValueError as v:
    print(v)
except Exception as e:
    print(e)

print("Thank You ")