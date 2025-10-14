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
    for letter in original_text:
        try:
            shifted_amount = alphabet.index(letter) + shift
            shifted_amount %= len(alphabet)
            text += alphabet[shifted_amount]
        except:
            text += letter
    print(f"Here is {operation}d text {text}")

caesar(original_text, shift, operation)