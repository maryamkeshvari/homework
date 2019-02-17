import random
class Chatbot:
    def __init__(self,standard_answers,question_answers):
        self.standard_answers=standard_answers
        self.question_answers=question_answers
    def answers(self,text):

        if "?" in text:
            random_index = random.randint(0, len(self.question_answers) - 1)
            print(self.question_answers[random_index])
        else:
            random_index = random.randint(0, len(self.standard_answers) - 1)
            print(self.standard_answers[random_index])

    def learn(self,text):
        if "?" in text:
            random_index = random.randint(0, len(self.question_answers) - 1)
            question_answers.append(random_index)
        else:
            random_index = random.randint(0, len(self.standard_answers) - 1)
            standard_answers.append(random_index)

standard_answers=["yes","no","it is interesting"]
question_answers=["good","bad","maybe","who knows","ok","only god know"]

chat=Chatbot(standard_answers,question_answers)
while True:
    text=str(input("input text: "))

    chat.answers(text)
