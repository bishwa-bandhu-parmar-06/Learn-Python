# 2. Write a program to accept marks of 6 students and display them in a sorted 
# manner.

marks = []
marks1 = int(input("Enter marks of student 1: "))
marks.append(marks1)
marks2 = int(input("Enter marks of student 2: "))
marks.append(marks2)
marks3 = int(input("Enter marks of student 3: "))
marks.append(marks3)
marks4 = int(input("Enter marks of student 4: "))
marks.append(marks4)
marks5 = int(input("Enter marks of student 5: "))
marks.append(marks5)
marks6 = int(input("Enter marks of student 6: "))
marks.append(marks6)

marks.sort()
print(marks)


