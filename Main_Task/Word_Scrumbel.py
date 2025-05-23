# the player has to unscramble a jumbled word from the words given in a list format.
import random

"""Logic:
1. Import random class
2. Create a list of words
3. Randomly pick the word from given list and store it in variable
4. Jumble the word using random.sample() function
5. Display the jumbled word to the player 
6. Guess the original word
7. Using if condition check if the guess is correct or not
"""

#List of words  
words = ['python', 'java', 'pytest', 'javascript' , 'automation', 'selenium', 'guvi']
#Randomly select a word from the list using random.choice() function
word = random.choice(words)
#Jumble the selected word
jumbled_word = ''.join(random.sample(word, len(word)))
#Display the jumbled word to the player
print("Jumbled word is: ", jumbled_word)
#Ask the player to guess the original word
guess = input("Guess the original word: ")
#Check if the guess is correct
if guess == word:
    print("Congratulations! You guessed the word correctly.")
else:
    print("Sorry, that's not correct. The original word was: ", word)
