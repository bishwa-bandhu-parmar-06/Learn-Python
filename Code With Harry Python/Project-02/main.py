'''
PROJECT 2 – THE PERFECT GUESS
We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.
Hint: Use the random module.
'''


import random

def perfect_guess():
    # Random number between 1 to 100
    number = random.randint(1, 100)
    guesses = 0
    user_guess = None

    print("Welcome to 'The Perfect Guess' Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    while user_guess != number:
        try:
            user_guess = int(input("Enter your guess: "))
            guesses += 1

            if user_guess > number:
                print("Lower number please ⬇️")
            elif user_guess < number:
                print("Higher number please ⬆️")
            else:
                print(f"🎉 Congratulations! You guessed it in {guesses} tries.")
        except ValueError:
            print("⚠️ Please enter a valid integer!")

# Run the game
perfect_guess()
