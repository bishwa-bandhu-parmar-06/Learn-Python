class Employee:
    language = "py" #this is class attribute
    salary = 1200000

harry = Employee()
print(harry.name, harry.language)

rohan = Employee()
rohan.name = "Rohan Singh" #this is instance attribute
print(rohan.name,rohan.salary, rohan.language)

# here name is the instance attribute and salary and language are the class attribute as they directly belong to the class