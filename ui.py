from tkinter import *
from quiz_brain import QuizBrain
from time import sleep
THEME_COLOR = "#375362"
WHITE = "#FFFFFF"


class QuizInterface:
    """
    Handles the graphical interface of the flashcard quiz.
    """
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", fg=WHITE, bg=THEME_COLOR,
                                 font=("Arial", 12, "bold"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg=WHITE)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_label = self.canvas.create_text(150, 125, width=280,
                                                      text="", anchor="center", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.get_next_question()

        true = PhotoImage(file="./images/true.png")
        false = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=true, command=lambda: self.get_answer("True"),
                                  borderwidth=0, highlightthickness=0, activebackground=THEME_COLOR)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false, command=lambda: self.get_answer("False"),
                                   borderwidth=0, highlightthickness=0, activebackground=THEME_COLOR)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()

    def get_answer(self, user_input):
        """
        Input is a boolean showing whether the user is correct or incorrect.
        Changes the background color of the card depending on the answer. Red for wrong, Green for correct.
        :param user_input: True or False user input
        """
        if self.quiz.check_answer(user_input):
            self.canvas.configure(bg="green")
            self.correct_answer()
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        """
        Changes the question text if there is still more, otherwise notifies the user and shows the final score.
        """
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text=q_text)
        else:
            self.canvas.itemconfig(self.question_label,
                                   text=f"You've reached the end of the quiz.\nYour final score was: {self.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def correct_answer(self):
        """
        Increase the score and update the label
        """
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")