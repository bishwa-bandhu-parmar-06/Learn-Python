# 3. Write a program to detect double space in a string. 

name = "Alice is a good boy"

name2 = "Alice is a good boy  "
double_space = name.find("  ")

print("Double space in Name : ",double_space)
print("Double space in Name2 : ", name2.find("  "))