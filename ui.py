from tkinter import *
from quiz_brain import QuizBrain

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
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=question_text)

    def answer_true(self):
        if self.quiz.check_answer('True'):
            self.score += 1
            self.score_label.config(text=f'score: {self.score}')
        self.get_next_question()

    def answer_false(self):
        if self.quiz.check_answer('False'):
            self.score += 1
            self.score_label.config(text=f'score: {self.score}')
        self.get_next_question()


