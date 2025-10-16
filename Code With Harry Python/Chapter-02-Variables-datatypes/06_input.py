# This code takes two inputs from the user and prints their sum.
# However, it does not convert the inputs to integers, so the sum will be a stringconcatenation.
# To fix this, we should convert the inputs to integers before summing them.
a = input("Enter a number: ")

b = input("Enter another number: ")

print("Number a is : ", a)
print("Number b is : ", b)

print("Sum of a and b is : ", a + b )


# Note: The above code will concatenate the inputs as strings.

# Fixing the code by converting inputs to integers
c = int(input("Enter a number: "))

d = int(input("Enter another number: "))

print("Number a is : ", c)
print("Number b is : ", d)

print("Sum of a and b is : ", c + d )