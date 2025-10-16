# Arithmentic Operators
# Addition
print(10 + 5)  # Output: 15
# Subtraction
print(10 - 5)  # Output: 5
# Multiplication
print(10 * 5)  # Output: 50
# Division
print(10 / 5)  # Output: 2.0
# Modulus
print(10 % 3)  # Output: 1
# Exponentiation
print(10 ** 2)  # Output: 100
# Floor Division
print(10 // 3)  # Output: 3



# Comparison Operators
# Equal to
print(10 == 10)  # Output: True
# Not equal to
print(10 != 5)  # Output: True
# Greater than
print(10 > 5)  # Output: True
# Less than
print(10 < 5)  # Output: False
# Greater than or equal to
print(10 >= 10)  # Output: True
# Less than or equal to
print(10 <= 5)  # Output: False


# Logical Operators
# Logical AND
print(True and False)  # Output: False
# Logical OR
print(True or False)  # Output: True
# Logical NOT
print(not True)  # Output: False


# Identity Operators
# is
print(10 is 10)  # Output: True
# is not
print(10 is not 5)  # Output: True


# Membership Operators
# in
print(5 in [1, 2, 3, 4, 5])
# Output: True
# not in
print(6 not in [1, 2, 3, 4, 5])  # Output: True


# Bitwise Operators
# Bitwise AND
print(10 & 5)  # Output: 0
# Bitwise OR
print(10 | 5)  # Output: 15
# Bitwise XOR
print(10 ^ 5)  # Output: 15
# Bitwise NOT
print(~10)  # Output: -11
# Bitwise Left Shift
print(10 << 2)  # Output: 40
# Bitwise Right Shift
print(10 >> 2)  # Output: 2



# Assignment Operators
# Simple Assignment
x = 10
print(x)  # Output: 10
# Add and Assign
x += 5
print(x)  # Output: 15
# Subtract and Assign
x -= 3
print(x)  # Output: 12
# Multiply and Assign
x *= 2
print(x)  # Output: 24
# Divide and Assign
x /= 4
print(x)  # Output: 6.0
# Modulus and Assign
x %= 2
print(x)  # Output: 0.

# Exponentiation and Assign
x **= 3
print(x)  # Output: 0.0
# Floor Division and Assign
x //= 1
print(x)  # Output: 0.0

# Ternary Operator
# Syntax: value_if_true if condition else value_if_false
x = 10
y = 20
result = x if x > y else y
print(result)  # Output: 20

# Chained Comparison
# Syntax: a < b < c
a = 5
b = 10
c = 15
print(a < b < c)  # Output: True

# Truth table for or logical operators
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# Truth table for and logical operators
# True and True = True
# True and False = False
# False and True = False
# False and False = False

# Truth table for not logical operator
# not True = False
# not False = True