# 7. If the names of 2 friends are same; what will happen to the program in problem 
# 6?


emptyDict = {}

name = input("Enter friends name : ")
lang = input("Enter friends language : ")
emptyDict.update({name : lang})

name = input("Enter friends name : ")
lang = input("Enter friends language : ")
emptyDict.update({name : lang})

name = input("Enter friends name : ")
lang = input("Enter friends language : ")
emptyDict.update({name : lang})

name = input("Enter friends name : ")
lang = input("Enter friends language : ")
emptyDict.update({name : lang})

print(emptyDict)

# it will update the old language with the new one 