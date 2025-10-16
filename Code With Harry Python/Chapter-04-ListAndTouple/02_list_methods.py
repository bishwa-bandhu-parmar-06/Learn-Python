friends = ["Apple", "Orange", 3, 4.55, True, "Grapes"]
print(friends)


# Lists Methods : 
friends.append("Alice")
print(friends)

friends.reverse()
print(friends)

l1 = [1, 44, 22, 34 , 12, 10, 21]
l1.sort()
print(l1)

l1.append(56)
print(l1)

l1.pop()
print(l1)

fruits = ['apple', 'banana', 'cherry']

fruits.append('orange')       # ['apple', 'banana', 'cherry', 'orange']
fruits.extend(['mango'])      # ['apple', 'banana', 'cherry', 'orange', 'mango']
fruits.insert(1, 'kiwi')      # ['apple', 'kiwi', 'banana', 'cherry', 'orange', 'mango']
fruits.remove('banana')       # ['apple', 'kiwi', 'cherry', 'orange', 'mango']
last = fruits.pop()           # returns 'mango'
index = fruits.index('kiwi')  # returns 1
count = fruits.count('apple') # returns 1
fruits.sort()                 # ['apple', 'cherry', 'kiwi', 'orange']
fruits.reverse()              # ['orange', 'kiwi', 'cherry', 'apple']
new_list = fruits.copy()      # Creates a shallow copy
fruits.clear()                # Now fruits = []
