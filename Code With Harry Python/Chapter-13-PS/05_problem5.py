
from functools import reduce
a = [1, 2, 34234, 53, 6236363, 738243, 65, 7534, 45, 55]

def greater(a, b):
    if(a > b):
        return a
    return b

print(reduce(greater,a))