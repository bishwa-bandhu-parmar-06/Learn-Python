class Employee:
    language = "Python" #this is class attribute
    salary = 1200000

    def getinfo(self):
        print(f"The Language is {self.language}, The salary is {self.salary}")

    def greet(self):
        print("good Morning")

    @staticmethod
    def greet1():
        print("good Morning")
harry = Employee()
harry.language = "JavaScript"
# print(harry.language)

harry.getinfo()
harry.greet()

harry.greet1()