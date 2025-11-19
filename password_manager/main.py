from tkinter import *
from tkinter import messagebox

FONT = ("Noto Sans", 13)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are details entered: \nEmail: {email}\nWebsite: {website} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
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
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()

email_entry = Entry(width=35, font=FONT)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "adarsh@email.com")
password_entry = Entry(width=21, font=FONT)
password_entry.grid(row=3, column=1, sticky="ew")


# Buttons

generate_password_button = Button(text="Generate Password", font=FONT)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", font=FONT, width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()