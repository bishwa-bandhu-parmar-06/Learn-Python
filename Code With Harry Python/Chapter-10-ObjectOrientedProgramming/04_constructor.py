class Employee:
    language = "Python" #this is class attribute
    salary = 1200000


    def __init__(self, name, salary, language):#as a dunder method whioch is automatically call
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an Object.")


    def getinfo(self):
        print(f"The Language is {self.language}, The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning.")
    
harry = Employee("Harry", 1300000, "Javascript")

print(harry.name, harry.salary)

