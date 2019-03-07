import random
class Chat1:
    def __init__(self,questions):
        self.questions=questions
    def question(self):
        question_text=question.pop(random.randint(0,len(self.questions)-1))

        return (question_text)

class Chat2:
    def __init__(self,standard_answers,question_answers,movies_answers,weather_answers,bye_answers,color_answers,cuntry_answers):
        self.standard_answers=standard_answers
        self.question_answers=question_answers
        self.movies_answers=movies_answers
        self.weather_answers=weather_answers
        self.bye_answers=bye_answers
        self.color_answers=color_answers
        self.cuntry_answers=cuntry_answers
    def replay(self,input_text):
        if "hi" in input_text:
            answer=random.randint(0,len(self.standard_answers)-1)
            print(self.standard_answers[answer])
        elif "how" in input_text:
            answer = random.randint(0, len(self.question_answers) - 1)
            print(self.question_answers[answer])
        elif "movie" in input_text:
            answer = random.randint(0, len(self.movies_answers) - 1)
            print(self.movies_answers[answer])
        elif "weather" in input_text:
            answer = random.randint(0, len(self.weather_answers) - 1)
            print(self.weather_answers[answer])
        elif "color" in input_text:
            answer = random.randint(0, len(self.color_answers) - 1)
            print(self.color_answers[answer])
        elif "where" in input_text:
            answer = random.randint(0, len(self.cuntry_answers) - 1)
            print(self.cuntry_answers[answer])
        else:
            answer = random.randint(0, len(self.bye_answers) - 1)
            print(self.bye_answers[answer])
standard_ans =[ "hi" ,"hello","hey","good morning","good afternoon","good evening"]
question_ans=["good","bad","fine","not bad"]
movies=["me after you","cunjorin","Cinderella","the notebook",'casablanca']
weather=['sunny',"raining","cloudy","foggy","snowy"]
colors=["red","green","yellow"]
bye=["bye","good bye","bye bye",'good night',"have a nice day","see you tomorrow","nice to see you"]
question=['what is your favorites movie ?','How is the weather ?','what is your favorites color ?',"where are you from ?"]
cuntry=["Iran","England","Armenia","Usa"]
i=0
chat=Chat1(question)
bot=Chat2(standard_ans,question_ans,movies,weather,bye,colors,cuntry)
while i<8:
    if i==0:
        input_text="hi"
        i+=1
    elif i==6:
        input_text="see you later. "
        i+=1
    elif i==1:
        input_text="how are you ?"
        i+=1
    else:
        input_text=chat.question()
        i+=1
    print(input_text)
    bot.replay(input_text)
    if i==7:
        break


