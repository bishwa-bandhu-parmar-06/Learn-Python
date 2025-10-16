# 4. Add a static method in problem 2, to greet the user with hello


# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.




class calculator: 
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"The Square is : {self.n * self.n}")

    def squareRoot(self):
        print(f"The Square Root is : {self.n ** 1/2}")

    def cube(self):
        print(f"The Cube is : {self.n * self.n * self.n}")

    @staticmethod
    def hello():
        print("Hello There!")

a = calculator(4)
a.hello()
a.square()
a.squareRoot()
a.cube()