import json
import random
import hangman_art

stages = hangman_art.stages

with open("wordlist.txt", 'r') as file:
    easy_words = file.read()
    easy_words = list(easy_words.splitlines())

with open("wordlist.json", 'r') as file:
    hard_words = json.load(file)

print(hangman_art.logo)

while True:
    mode = input("\nSelect game mode 'EASY' or 'HARD', enter 'QUIT' to quit game: ")

    if mode[0] == 'e':
        words = easy_words
        break
    elif mode[0] == 'h':
        words = hard_words
        break
    elif mode[0] == 'q':
        print("\nThanks for playing")
        break
    else:
        print("\nSelect correct game mode.")

word = str(random.choice(words)).lower()


length_of_word = len(word)
blank = "_" * length_of_word
print()
print(blank)

correct_letter = []

lives = 6

game_over = False

while not game_over:
    guess = input("Enter your guess: ").lower()

    if guess in correct_letter:
        print(f"You've already guessed {guess}")

    display = ""
    for letter in word:
        if letter == guess:
            display += guess
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print()
    print(display)
    print()

    if guess not in correct_letter:
        lives -= 1
        print()
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        print(f"You have {lives} lives left.\n")
        if lives == 0:
            game_over = True
            print("You have exhausted all your lives.")
            print("************GAME-OVER************")

    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("Cograulations you guessed all the letters.")
    
print(f"The word was '{word}'")

