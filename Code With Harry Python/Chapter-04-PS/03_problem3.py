# 3. Check that a tuple type cannot be changed in python.

a = (1, 2, 3, 4, 5, "alice")
a[0] = 6 #TypeError: 'tuple' object does not support item assignment
print(a)