# String is a data type in python. 
# String is a sequence of characters enclosed in quotes. 
# # Strings are immutable, meaning once created, they cannot be changed.
# Strings can be used to represent text, numbers, and other characters.

# String Slices
# A string slice is a substring of a string.
# Example of a string slice
s = "Hello, World!"
# Getting a substring from index 0 to 4 (exclusive)

print("Original String: ", s)
print("Substring: ", s[:5])
substring = s[0:5]  # 'Hello'
print("Substring: ",substring)
# Getting a substring from index 7 to the end
substring2 = s[7:]  # 'World!'
print("Substring from index 7: ", substring2)
print("Character 1 : ", s[1])  # 'e'
print("Character 2 : ", s[2])  # 'l'
print("Character 3 : ", s[3])  # 'l'
print("Character 4 : ", s[4])  # 'o'

# Negative Indexing
# Negative indexing allows you to access characters from the end of the string.
print("Last character: ", s[-1])  # '!'
print("Second last character: ", s[-2])  # 'd'
# String Concatenation
# Concatenation is the process of joining two or more strings together.
# Example of string concatenation
s1 = "Hello"
s2 = "World"
s3 = s1 + ", " + s2 + "!"  # 'Hello, World!'
print("Concatenated String: ", s3)

# String Repetition
# Repetition is the process of repeating a string multiple times.
# Example of string repetition
s4 = "Hello" * 3  # 'HelloHelloHello'
print("Repeated String: ", s4)





# Strings can be enclosed in single quotes, double quotes, or triple quotes.
# Example of a string enclosed in single quotes
a  = 'Hello, World!'
# Example of a string enclosed in double quotes
b = "Hello, World!"
# Example of a string enclosed in triple quotes
c = """Hello,World!"""
# Example of a string enclosed in triple quotes with new lines
d = '''Hello,World!'''
# Example of a string with escape characters    
e = 'Hello, \nWorld!'  # \n is a newline character
f = "Hello, \tWorld!"  # \t is a tab character
# Example of a string with both single and double quotes
g = 'He said, "Hello, World!"'
h = "It's a beautiful day!"
# Example of a string with backslash
i = "This is a backslash: \\"


# String Length
# The length of a string can be found using the len() function.
length = len(s)  # 13
print("Length of the string: ", length)
