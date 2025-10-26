from data import Opentb
from question_model import Question
from quiz_brain import QuizBrain
from random import shuffle
from html import unescape
from art import logo

logo = logo
print(logo)

data = Opentb()
question_bank = []


for i in range(10):
    question = unescape(data.data['results'][i]['question'])
    answer = unescape(data.data['results'][i]['correct_answer'])
    category = unescape(data.data['results'][i]['category'])
    new_question = Question(question, answer, category)
    question_bank.append(new_question)


shuffle(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    print('\n')

print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")