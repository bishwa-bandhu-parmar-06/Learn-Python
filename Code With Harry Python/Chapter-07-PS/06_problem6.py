# 6. Write a program to calculate the factorial of a given number using for loop. 
num = int(input("Enter a number: "))

if(num == 1 or num == 0):
    print("Factorial of", num, "is: 1")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    print("Factorial of", num, "is", factorial)