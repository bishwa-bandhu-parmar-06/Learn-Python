import random

'''
1 for snake
-1 for water 
0 for gun
'''

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Get computer choice
computer = random.choice([-1, 0, 1])

# Get user input with prompt
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Check if input is valid
if youstr not in youDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw!")
    elif (computer == -1 and you == 1) or \
         (computer == 1 and you == 0) or \
         (computer == 0 and you == -1):
        print("You win!")
    else:
        print("You lose!")
