# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = int(input("Enter The Number You Want To Print The Table of : "))

# table = [i * num for i in myList] 
table = [i * num for i in range(1, 11)] 

with open("Tables.txt", "a") as f:
    f.write(str(table) + "\n")

