from Question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = Quiz_Brain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("quiz is completed")
print(f"your final score was : {quiz.score}/{quiz.question_number}")

