from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg='white', font='bold')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text='Hellooooo',
                                                     fill=THEME_COLOR,
                                                     font=('Areal', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        self.right_image = PhotoImage(file="./images/false.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, command=self.false_pressed)
        self.right_button.grid(row=2, column=1)

        self.left_image = PhotoImage(file="./images/true.png")
        self.left_button = Button(image=self.left_image, highlightthickness=0, command=self.true_pressed)
        self.left_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state='disabled')
            self.left_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.canvas.after(1000, self.get_next_question)
