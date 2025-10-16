# 3. Attempt problem 1 using while loop.

# 1. Write a program to print multiplication table of a given number using for loop. 

num = int(input("Display multiplication table of?: "))

i = 1
while(i < 11):
    print(num, "X", i, "=", num*i)
    i += 1
