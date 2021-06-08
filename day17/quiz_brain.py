from question_model import questionBank


class QuizBrain:
    def __init__(self, qList):
        self.questionNumber = 0
        self.qList = qList
        self.score = 0

    def leftQuestions(self):
        return self.questionNumber < len(self.qList)

    def nextQuestion(self):
        print(f'Q.{self.questionNumber + 1}: {self.qList[self.questionNumber].text}? (True / False)')
        correct = self.qList[self.questionNumber].answer
        inp = input('--> ')
        if inp == correct:
            print('Nice Job!')
            self.score += 1
        else:
            print('Wrong')
            self.score -= 1

        print(f'Current score: {self.score} /////\n')
        self.questionNumber += 1


qb = QuizBrain(questionBank)

while qb.leftQuestions():
    qb.nextQuestion()

print('======================')
print(f'Final score: {qb.score}')
print('======================')

