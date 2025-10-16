# 7. Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end = "")
    for j in range(1, 2 * i):
        print("*", end = "")
    print()
    

