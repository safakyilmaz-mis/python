#This file will help you to create app which can provide quiz game

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    Question.text = question_data[i]["question"]
    Question.answer = question_data[i]["correct_answer"]
    text = Question.text
    answer = Question.answer
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while QuizBrain.still_has_question(quiz):
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {QuizBrain.total_score(quiz)}")
print("or")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
