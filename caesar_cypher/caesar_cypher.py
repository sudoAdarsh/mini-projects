import string
import art

logo = art.logo
alphabet = string.ascii_lowercase
alphabet = list(alphabet)

print(logo)

operation = input("Choose the operation 'Encode/decode': ")
original_text = input("Enter the text: ")
shift = int(input("Enter shift amount: "))

def caesar (original_text, shift, operation):
    text = ""
    if operation.startswith('d'):
        shift *= -1
        if letter not in alphabet:
            text += letter
        else:
            for letter in original_text:
                shifted_amount = alphabet.index(letter) + shift
                shifted_amount %= len(alphabet)
                text += alphabet[shifted_amount]
                text += letter
    print(text)

caesar(original_text, shift, operation)