# Importing necessary modules
import string
import random 

# Define character sets
letters = string.ascii_letters
numbers = string.digits
symbols = ['!', '#', '$', '&', '*', '%']

# Get user input for password composition
num_letters = int(input("How many letters you would like in your password: "))
num_symbols = int(input("How many symbols: "))
num_digits = int(input("How many digits: "))

# Generate the password list based on user input
password_list = (
    random.choices(letters, k=num_letters) +
    random.choices(symbols, k=num_symbols) + 
    random.choices(numbers, k=num_digits)
)

# Shuffle and join the list to create the final password
random.shuffle(password_list)
password = "".join(password_list)

# Output the generated password
print(f"Your password is \"{password}\"")
