from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0

        self.score_label = Label(text=f'score: {self.score}', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.question = self.canvas.create_text(150, 150, text="some stuff", font=("Arial", 20, "italic"), width=270)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions()
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def answer_true(self):
        self.give_feedback(self.quiz.check_answer('True'))
        #     self.score += 1
        #     self.score_label.config(text=f'score: {self.score}')
        #     self.canvas.itemconfig(self.question, text="Correct!")
        #     self.window.update()
        #     self.window.after(1000)
        # else:
        #     self.canvas.itemconfig(self.question, text="Incorrect!")
        #     self.window.update()
        #     self.window.after(1000)
        # self.get_next_question()

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer('False'))
        # if self.quiz.check_answer('False'):
        #     self.score += 1
        #     self.score_label.config(text=f'score: {self.score}')
        #     self.canvas.itemconfig(self.question, text="Correct!")
        #     self.window.update()
        #     self.window.after(1000)
        #     self.canvas.itemconfig(self.question, text="Correct!")
        # else:
        #     self.canvas.itemconfig(self.question, text="Incorrect!")
        #     self.window.update()
        #     self.window.after(1000)
        #     self.canvas.itemconfig(self.question, text="Correct!")
        # self.get_next_question()

    def give_feedback(self, is_correct):
        if is_correct:
            self.score += 1
            self.score_label.config(text=f'score: {self.score}')
            self.canvas.itemconfig(self.question, text="Correct!")
            self.window.update()
            self.canvas.config(bg='green')
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.itemconfig(self.question, text="Incorrect!")
            self.window.update()
            self.canvas.config(bg='red')
            self.window.after(1000, self.get_next_question)




