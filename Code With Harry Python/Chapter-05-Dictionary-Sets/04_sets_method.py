# Sets Methods

a = {1, 2, 3}
b = {3, 4, 5}

a.add(6)               # {1, 2, 3, 6}
a.update([7, 8])       # {1, 2, 3, 6, 7, 8}
a.remove(1)            # Removes 1
a.discard(10)          # Does nothing (no error)
print(a.pop())         # Removes a random element
a.clear()              # a becomes empty set

# Set operations
x = {1, 2, 3}
y = {2, 3, 4}

print(x.union(y))                 # {1, 2, 3, 4}
print(x.intersection(y))          # {2, 3}
print(x.difference(y))            # {1}
print(x.symmetric_difference(y))  # {1, 4}

# Comparison
print(x.issubset({1, 2, 3, 4}))   # True
print(x.issuperset({1, 2}))       # True
print(x.isdisjoint({10, 20}))     # True


