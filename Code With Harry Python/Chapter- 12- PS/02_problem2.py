# 2. Write a program to print third, fifth and seventh element from a list using enumerate
# function.


myList = [1, 2, 3, 4, 5, 6, 7, 8]


for index, item in enumerate(myList):
    if index == 2 or index == 4 or index == 6:
        print(item)