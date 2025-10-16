# 5. Label the program written in problem 4 with comments. 


import os

directory_path = '/'  # You can change this to any directory you want to list

contents = os.listdir(directory_path)

for item in contents:
    print(item)
