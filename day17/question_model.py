from data import question_data


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


questionBank = []


for question in question_data:
    q = Question(question['text'], question['answer'])
    questionBank.append(q)

