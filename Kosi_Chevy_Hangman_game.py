# Chevy Hangman Game
# Simple text based hangman where you guess letters

import random

# list of 5 words for the game
word_list = ["python", "coding", "laptop", "program", "script"]

# pick a random word
secret_word = random.choice(word_list)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Chevy Hangman!")
print("Guess the word one letter at a time.")
print("You can only get 6 letters wrong.\n")

# show the blanks at the start
display = []
for letter in secret_word:
    display.append("_")

print("Word: " + " ".join(display))

# main game loop
while wrong_guesses < max_wrong and "_" in display:
    guess = input("Enter a letter: ").lower().strip()

    # check if its a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already tried that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
        # update the display
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses = wrong_guesses + 1
        print("Wrong! You have " + str(max_wrong - wrong_guesses) + " tries left.")

    print("Word: " + " ".join(display))
    print("Guessed so far: " + ", ".join(guessed_letters))
    print()

# check if won or lost
if "_" not in display:
    print("You won! The word was " + secret_word)
else:
    print("Game over. The word was " + secret_word)
    print("Better luck next time!")
    