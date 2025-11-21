import pandas

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabets_dict = {row.letter : row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

while True:
    try:
        word = input("Enter a word: ").upper().strip()
        word_list = list(word)
        word_nato_list = [alphabets_dict[letter] for letter in word_list]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(word_nato_list)
        break