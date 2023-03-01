from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for ques in question_data:
    n_Q = ques["question"]
    n_A = ques["correct_answer"]
    new_question = Question(n_Q, n_A)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while QuizBrain.still_has_questions and quiz.question_number < 10:
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score: {quiz.score}/{quiz.question_number}")
