class Person:
    def __init__(self,shoping_time,talk_time):
        self.shoping_time=shoping_time
        self.talk_time=talk_time

def who_is_it(person):
    if person.shoping_time>180 and person.talk_time >20:
        print("she is woman.")
    else:
        print("he is a man.")

class Animels:
    def __init__(self,weight,length):
        self.weigth=weight
        self.length=length
def what_is_it(animel):
    if animel.weigth > 10 and animel.length > 60:
        print("it is a dog.")
    else:
        print("it is a cat.")


allen=Person(182,5)
maryam=Person(200,55)
who_is_it(allen)
who_is_it(maryam)

oskar=Animels(2,40)
grey=Animels(18,90)
what_is_it(grey)
what_is_it(oskar)