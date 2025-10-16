# # touple methods
# In Python, a tuple is an immutable and ordered data structure. Since it cannot be changed after creation (unlike lists), it supports fewer methods.

t = (1, 2, 3, 2, 4, 2)

print(t.count(2))     # Output: 3 (2 appears 3 times)
print(t.index(3))     # Output: 2 (3 is at index 2)
print(t.index(2, 2))  # Output: 3 (2 after index 2)
print(len(t))