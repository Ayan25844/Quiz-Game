from data import question_data
from quiz_brain import QuizBrain
from question_model import Question
question_bank=[]
for i in question_data:
    question_bank.append(Question(i["text"],i["answer"]))
quiz=QuizBrain(question_bank)
while quiz.Still_has_questions():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")