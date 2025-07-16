from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)

        self.score=0
        self.score_label=Label(text=f"Score: {self.score}",bg=THEME_COLOR,font=("Ariel",13,"normal"))
        self.score_label.grid(row=0,column=1)

        self.canvas_setup=Canvas(width=300,height=250,highlightthickness=0)
        self.text= self.canvas_setup.create_text(150,125,text="question_text",width=280,font=("Ariel",17,"italic"))
        self.canvas_setup.grid(row=1,column=0,columnspan=2,pady=20,padx=20)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0,bg=THEME_COLOR,command=self.correct_answer)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0,bg=THEME_COLOR,command=self.wrong_answer)
        self.false_button.grid(row=2, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas_setup.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        q_text= self.quiz.next_question()
        self.canvas_setup.itemconfig(self.text,text=q_text)

    def correct_answer(self):
        self.feedback(self.quiz.check_answer("True"))

    def wrong_answer(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self,is_right):
        if is_right:
            self.canvas_setup.config(bg="green")
        else:
            self.canvas_setup.config(bg="red")

        self.window.after(1000,self.get_question)
        

