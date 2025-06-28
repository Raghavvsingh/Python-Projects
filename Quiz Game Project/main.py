from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

length_qdata = len(question_data)

for i in range(0,length_qdata):
    q_text=question_data[i]["text"]
    q_answer=question_data[i]["answer"]
    new_question=Question(q_text,q_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    print("\n")

print("You've Completed the Quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")

