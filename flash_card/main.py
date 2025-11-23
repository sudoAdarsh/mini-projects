from tkinter import *
import pandas
import os

BACKGROUND_COLOR = "#B1DDC6"
file = "250-words.csv"
file = "french_words.csv"
to_learn_file= "to_learn.csv"
row = {}


def learn_card():
    to_learn = [row.French.iloc[0], row.English.iloc[0]]
    new_df = pandas.DataFrame([to_learn], columns=["French", "English"])
    if not os.path.exists(to_learn_file):
        new_df.to_csv("to_learn.csv",mode="w", header=True, index=False)
    else:
        new_df.to_csv("to_learn.csv",mode="a", header=False, index=False)
    next_card()


def next_card():
    global row, flip_timer
    window.after_cancel(flip_timer)
    df = pandas.read_csv(file)
    row = df.sample(n=1)
    in_french = row.French.iloc[0]
    canvas.itemconfig(card_tittle, text="French", fill="black")
    canvas.itemconfig(card_word, text=in_french, fill="black")
    canvas.itemconfig(card_bg, image=front_card_img)
    flip_timer = window.after(3000, show_card)


def show_card():
    in_english = row.English.iloc[0]
    canvas.itemconfig(card_tittle, text="English", fill="white")
    canvas.itemconfig(card_word, text=in_english, fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)




################### UI SETUP ######################

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, show_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=front_card_img)
card_tittle = canvas.create_text(400, 150, text="French",font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)



cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=learn_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()