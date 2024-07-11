from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuestionInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # Score Label
        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR, font=("Arial", 12, 'normal'))
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas_box = Canvas(width=300, height=250, bg="white")
        self.canvas_text = self.canvas_box.create_text(150, 125, width=280, text="Sample Text", fill="black",
                                                       font=("Arial", 20, 'italic'))
        self.canvas_box.grid(row=1, column=0, columnspan=2, pady=50)

        # Right Button
        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, border=0,
                                   command=self.true_pressed)
        self.right_button.grid(row=2, column=0)

        # Wrong Button
        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, border=0,
                                   command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas_box.config(bg="white")
        if self.quiz.still_has_question():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas_box.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas_box.itemconfig(self.canvas_text, text="You've reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas_box.config(bg="green")
            self.quiz.score += 1
        else:
            self.canvas_box.config(bg="red")
        self.window.after(1000, self.get_next_question)
