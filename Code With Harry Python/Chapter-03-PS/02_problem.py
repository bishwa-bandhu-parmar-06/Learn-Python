# 2. Write a program to fill in a letter template given below with name and date. 
# letter = '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# ''' 

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

# name = input("Enter Your Name : ")
# date = input("Enter Date : ")
# letter = letter.replace("<|Name|>", name)
# letter = letter.replace("<|Date|>", date)
# print(letter)

print(letter.replace("<|Name|>", "Bikash").replace("<|Date|>", "16th July 2025"))