#computer randomly selects a number between 1 and 100 and asks the player  to guess it.
import random

"""Logic:
1. Import random class
2. We need to select a number between 1 and 50
3. Guess the number 
4. Using if condition check if the guess is correct or not
5. If the guess is too low or too high, give a hint to the player
"""
#Randomly select a number between 1 and 50
secret_number = random.randint(1, 50)
guess = None
attempts = 0

#Loop until the player guesses the number
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Your Guess is too low")
    elif guess > secret_number:
        print("your Guess is too high")
    else:
        print("Congratulations! You guessed the number ")

