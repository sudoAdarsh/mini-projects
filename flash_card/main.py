from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
back_image = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=back_image)
canvas.pack()


window.mainloop()