from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain
from ui import QuestionInterface

question_bank = []

for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Questions(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuestionInterface(quiz)

# while quiz.still_has_question():
#     quiz.next_question()
