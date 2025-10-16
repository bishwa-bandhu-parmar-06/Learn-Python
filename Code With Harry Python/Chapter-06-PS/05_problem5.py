# 5. Write a program which finds out whether a given name is present in a list or not. 


nameList = ["Harry", "Sohan", "Sachin", "Rahul"]
name = input("Enter a name to check: ")

if(name in nameList):
    print("Name is present in the list")
else:
    print("Name is not present in the list")