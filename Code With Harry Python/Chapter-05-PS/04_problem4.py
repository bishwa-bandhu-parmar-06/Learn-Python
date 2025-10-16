# 4. What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations?

s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(len(s)) # 2

# 20 == 20.0 = true
# In Python sets, the comparison 20 == 20.0 evaluates to True, and this has a unique effect when adding these values to a set.

# 20 is an int

# 20.0 is a float

# But:

# python
# Copy code
# 20 == 20.0   # ✅ True


"""
🧠 What happens in a set?
Sets store unique values. When Python compares items for uniqueness in a set, it uses:

__eq__() (equality check)

and __hash__() (hash value)

Since 20 == 20.0 and both hash(20) == hash(20.0), they are treated as the same element.
"""