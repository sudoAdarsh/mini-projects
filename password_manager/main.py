from tkinter import *
from tkinter import messagebox
import pyperclip
import string
import random
import json

FONT = ("Noto Sans", 13)


# --------------------------- SHOW SAVED PASSWORD --------------------------------#

def search():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            all_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="You haven't saved any passwords yet.")
    else:
        try:
            data = all_data.get(website)
            email = data['email']
            password = data['password']
        except TypeError:
            messagebox.showinfo(title="Oops", message=f"You haven't saved any data for website {website}\nPlease save your password before fetching it.")
        else:
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def random_password():
    # Define character sets
    letters = string.ascii_letters
    numbers = string.digits
    symbols = ['!', '#', '$', '&', '*', '%']

    # Get user input for password composition
    num_letters = random.randint(8,10)
    num_symbols = random.randint(2,4)
    num_digits = random.randint(2,4)

    # Generate the password list based on user input
    password_list = (
        random.choices(letters, k=num_letters) +
        random.choices(symbols, k=num_symbols) + 
        random.choices(numbers, k=num_digits)
    )

    # Shuffle and join the list to create the final password
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0 , END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password 
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are details entered: \nEmail: {email}\nWebsite: {website} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)

            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                data.update(new_data)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                pyperclip.copy(password)
                clear_password()

def clear_password():
    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=360, height=360)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(180, 180, image=logo_image)
canvas.grid(row=0, column=0, columnspan=3)


# Labels

website_label = Label(text="Website: ", font=FONT)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ", font=FONT)
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ", font=FONT)
password_label.grid(row=3, column=0)


# Entries

website_entry = Entry(width=35, font=FONT)
website_entry.grid(row=1, column=1, sticky="ew")
website_entry.focus()

email_entry = Entry(width=35, font=FONT)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "adarsh@email.com")

password_entry = Entry(width=21, font=FONT)
password_entry.grid(row=3, column=1, sticky="ew")


# Buttons

generate_password_button = Button(text="Generate Password", font=FONT, command=random_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", font=FONT, width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

search_button = Button(text="Search", font=FONT, command=search)
search_button.grid(row=1, column=2, sticky="ew")

window.mainloop()