# 10. Write a program to print multiplication table of n using for loops in reversed 
# order. 


n = int(input("Enter a Number : "))

for i in range(10, 0, -1):
    print(n, "X", i, "=", n*i)