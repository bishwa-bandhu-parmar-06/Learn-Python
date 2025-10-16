s = "helloworld"

# Slicing with skip
sliced = s[1:8:2]  # Start at index 1, end before index 8, step by 2
print("Sliced String with skip: ", sliced)  # 'elwr'

word = "Python"
word_sliced = word[0:2]  # Start at index 0, end before index 6, step by 2
print("Sliced Word with skip: ", word_sliced)

word_sliced1 = word[0:]
print("Sliced Word from start: ", word_sliced1)  # 'Python'

print("Sliced Word with skip: ", word[:6])