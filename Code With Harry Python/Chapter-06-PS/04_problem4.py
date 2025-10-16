# 4. Write a program to find whether a given username contains less than 10 
# characters or not.

username = input("Enter your username: ")

usernameLength = len(username)
if(usernameLength < 10):
    print("Username is less than 10 characters")
else:
    print("Username is greater than 10 characters")