import random
class Chatbot:
    """it is a simple chatbot."""
    def __init__(self,standard_answers,question_answers,start_aqnswers,end_answers):
        self.standard_answers=standard_answers
        self.question_answers=question_answers
        self.start_ansers=start_aqnswers
        self.end_answers = end_answers
    def answers(self,text):
        """this is a function for answer your question ."""
        if "?" in text:
            random_index = random.randint(0, len(self.question_answers) - 1)
            print(self.question_answers[random_index])
        elif text in start_answers:
            random_index = random.randint(0, len(self.start_ansers) - 1)
            print(self.start_ansers[random_index])
        elif text in end_answers:
            random_index = random.randint(0, len(self.end_answers) - 1)
            print(self.end_answers[random_index])
        else:
            random_index = random.randint(0, len(self.standard_answers) - 1)
            print(self.standard_answers[random_index])

start_answers=["hello","hi","hey","good morning","good afternoon","good evening"]
standard_answers=["yes","no","maybe","ok","sure","i hope"]
question_answers=["good","bad","excellent"]
end_answers=["bye","good bye","bye bye",'good night',"have a nice day","see you tomorrow"]
chat=Chatbot(standard_answers,question_answers,start_answers,end_answers)
while True:
    text=str(input("input text: "))
    chat.answers(text)
    if text =="end":
        break
