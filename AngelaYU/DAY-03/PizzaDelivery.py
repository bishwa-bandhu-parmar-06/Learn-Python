print("Welcome to the Python Pizza Deliveries!")
size = input("What size Pizza Do You Want? : S, M, L : ")
add_paperoni = input("Do You Want Paperoni? Y or N : ")
extra_cheese = input("Do You Want Extra Cheese? Y or N : ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_paperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your Final Bill is ${bill}")