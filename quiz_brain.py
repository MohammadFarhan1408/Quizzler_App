import html


class QuizBrain:
    def __init__(self, question_list):
        self.current_question = None
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.current_question.text)
        return question_text
        # user_answer = input(f"Q.{self.question_number}: {question_text} (True/False): ")
        # self.check_answer(user_answer, self.current_question.answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            # self.score += 1
            return True
        else:
            return False

