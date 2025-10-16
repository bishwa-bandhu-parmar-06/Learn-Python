# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up!

words = {
    "ball" : "Gend",
    "bat": "Balla",
    "cat": "billi",
    "apple": "sev",
    "mango" : "Aam"
}

user_words = input("Enter english Words to Know Hindi : ")

print(words.get(user_words))
