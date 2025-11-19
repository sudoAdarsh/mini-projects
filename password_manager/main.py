from tkinter import *

FONT = ("Noto Sans", 13)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=360, height=360)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(180, 180, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)

website_entry = Entry(width=35, font=FONT)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")

email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(row=2, column=0)

email_entry = Entry(width=35, font=FONT)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

password_entry = Entry(width=21, font=FONT)
password_entry.grid(row=3, column=1, sticky="ew")

generate_password_button = Button(text="Generate Password", font=FONT)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", font=FONT, width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()