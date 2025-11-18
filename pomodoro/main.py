import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier Prime"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 8 == 0:
        count = long_break_sec
    elif reps % 2 == 0:
        count = short_break_sec
    else:
        count = work_sec
    
    count_down(count)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{count_minute:02}:{count_seconds:02}")
    if count >= 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)


button1 = Button(text="Start", highlightthickness=0, command=start_timer)
button1.grid(row=2, column=0)

button2 = Button(text="Reset", highlightthickness=0)
button2.grid(row=2, column=2)

label2 = Label(text="✔", font=(FONT_NAME, 25), bg=YELLOW, fg=GREEN)
label2.grid(row=3, column=1)

window.mainloop()