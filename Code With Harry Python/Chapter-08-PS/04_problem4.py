# 4. Write a recursive function to calculate the sum of first n natural numbers. 

def sum_natural_numbers(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_natural_numbers(n-1)
    
n = int(input("Enter a number: "))
print("Sum of first", n, "natural numbers is:", sum_natural_numbers(n))

                                    