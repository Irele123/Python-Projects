from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dictionaries in question_data:
    text = dictionaries["text"]
    answer = dictionaries["answer"]
    obj = Question(text, answer)
    question_bank.append(obj)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: ({quiz.score}/{quiz.question_number})")