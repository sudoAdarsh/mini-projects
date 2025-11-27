from tkinter import *
from quiz_brain import QuizBrain
import os

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.Quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        self.score_label = Label(text="Score:0", bg=THEME_COLOR, fg="white", font=("Courier Prime", 16))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=450, height=500, bg="white")
        self.q_text = self.canvas.create_text(
            225,
            250,
            width=430,
            text="Some question text here and some there",
            font=("Arial", 23, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        base_path = os.path.dirname(__file__)

        true_image = PhotoImage(file=os.path.join(base_path, 'images', 'true.png'))
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file=os.path.join(base_path, 'images', 'false.png'))
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()
    
    def next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.Quiz.score}")
        if self.Quiz.still_has_questions():
            new_ques = self.Quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=new_ques)
        else:
            self.canvas.itemconfig(self.q_text, text=f"Quiz Completed \nFinal Score: {self.Quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        is_right = self.Quiz.check_answer("true")
        self.give_feedback(is_right)

    def is_false(self):
        is_right = self.Quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.next_question)
