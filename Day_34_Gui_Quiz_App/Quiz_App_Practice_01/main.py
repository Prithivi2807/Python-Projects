from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for ques_var in question_data:
  questions = ques_var["question"]
  answers = ques_var["correct_answer"]
  new_question= Question(q_text=questions, q_answer=answers)
  question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
  quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")