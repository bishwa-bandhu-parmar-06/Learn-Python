class Employee:
    company = "ITC"
    name= "Alice"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}.")

class coder:
    language= "Python"
    def printLanguage(self):
        print(f"Out of All language here is your language : {self.language}")
     
class Programmer(Employee, coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language.")
        

a = Employee()
b = Programmer()


b.show()
b.printLanguage()
b.showLanguage()
print(a.company, b.company)