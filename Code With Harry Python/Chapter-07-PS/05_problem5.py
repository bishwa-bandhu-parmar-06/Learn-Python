# 5. Write a program to find the sum of first n natural numbers using while loop. 
num = int(input("Enter a number: "))

i = 1

if( i <= 0):
    print("Enter a positive number")
else:
    sum = 0
    while(i <= num):
        sum += i
        i += 1
    print("The sum of Natural Number is", sum)