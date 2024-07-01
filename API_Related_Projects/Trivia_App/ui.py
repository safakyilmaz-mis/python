from tkinter import *
from quiz_brain import QuizBrain

import question_model

THEME_COLOR = "#375362"
RED = "#FF0000"
GREEN = "#008000"
WHITE = "#FFFFFF"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.label = Label(self.window, text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font='Helvetica 15 bold')
        self.label.grid(row=1, column=2, pady=20)

        self.canvas = Canvas(self.window, width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, fill=THEME_COLOR,
                                                     font='Helvetica 20 italic')

        self.canvas.grid(row=2, column=1, columnspan=2, padx=20, pady=20)

        photoImg = PhotoImage(file="../Trivia_Question_App/images/true.png")
        self.correct_button = Button(self.window, image=photoImg, highlightthickness=0,
                                     command=self.true_pressed)

        self.correct_button.grid(row=3, column=1, padx=20, pady=20, sticky="e")

        photoImg2 = PhotoImage(file="../Trivia_Question_App/images/false.png")
        self.false_button = Button(self.window, image=photoImg2, highlightthickness=0,
                                   command=self.false_pressed)

        self.false_button.grid(row=3, column=2, padx=20, pady=20, sticky="w")
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=WHITE, highlightthickness=0)
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))
        self.canvas.itemconfig(self.question_text, fill=WHITE)

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))
        self.canvas.itemconfig(self.question_text, fill=WHITE)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN, highlightthickness=0)
            self.canvas.itemconfig(self.question_text, fill=WHITE)
        else:
            self.canvas.config(bg=RED, highlightthickness=0)
            self.canvas.itemconfig(self.question_text, fill=WHITE)
        self.window.after(1000, self.get_next_question)
