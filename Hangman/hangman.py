"""
Hangman Game 🎯
---------------
A simple terminal-based Hangman game with two modes:
EASY (words from a text file) and HARD (words from a JSON file).

Author: Adarsh Upadhyay
"""

import json
import random
import hangman_art  # Custom module containing 'stages' and 'logo'

# Load the ASCII art stages for hangman visuals
stages = hangman_art.stages

# ---------------------------
# Load words for both modes
# ---------------------------

# Load easy words from text file (one word per line)
with open("wordlist.txt", 'r') as file:
    easy_words = file.read().splitlines()

# Load hard words from JSON file (from a list)
with open("wordlist.json", 'r') as file:
    hard_words = json.load(file)

# Display the game logo
print(hangman_art.logo)

# ---------------------------
# Game Mode Selection
# ---------------------------
while True:
    mode = input("\nSelect game mode 'EASY' or 'HARD', enter 'QUIT' to quit game: ").lower()

    if mode.startswith('e'):
        words = easy_words
        lives = 5  # Easier mode → more lives
        break
    elif mode.startswith('h'):
        words = hard_words
        lives = 5  # Harder mode → fewer lives
        break
    elif mode.startswith('q'):
        print("\nThanks for playing!")
        exit()
    else:
        print("\nSelect correct game mode (EASY / HARD / QUIT).")

# ---------------------------
# Game Setup
# ---------------------------

# Choose a random word and prepare game variables
word = str(random.choice(words)).lower()
length_of_word = len(word)
blank = "_" * length_of_word
print("\n" + blank)

correct_letter = []   # Tracks letters guessed correctly
guessed_letters = []  # Tracks all guesses (correct + incorrect)
game_over = False

# ---------------------------
# Main Game Loop
# ---------------------------
while not game_over:
    guess = input("Enter your guess: ").lower()

    # Input validation — single alphabet only
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.\n")
        continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try another letter.\n")
        continue
    else:
        guessed_letters.append(guess)

    # Create the display with guessed letters revealed
    display = ""
    for letter in word:
        if letter == guess:
            display += guess
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print("\n" + display + "\n")

    # Handle incorrect guess
    if guess not in word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        print(f"You have {lives} lives left.\n")

        # End game if lives run out
        if lives == 0:
            game_over = True
            print("You have exhausted all your lives.")
            print("************ GAME OVER ************")

    # Show hangman stage corresponding to remaining lives (safe index)
    if lives >= 0 and lives < len(stages):
        print(stages[lives])

    # Check win condition
    if "_" not in display:
        game_over = True
        print("🎉 Congratulations! You guessed all the letters!")

# ---------------------------
# Game End
# ---------------------------
print(f"The word was '{word}'.")
print("Thanks for playing! See you next time 👋")
