# Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.  

import os

directory_path = '/'  # You can change this to any directory you want to list

contents = os.listdir(directory_path)

for item in contents:
    print(item)
# This will print the names of all files and directories in the specified path.
# If you want to print the full path, you can modify the print statement: