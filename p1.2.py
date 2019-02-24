class Person:
    def __init__(self,height,weight,hair_length):
        self.heigth=height
        self.weight=weight
        self.hair_length=hair_length

def recognaiz(person):
    if person.heigth >170 and person.weight >70 and person.hair_length<30:
        print("he is a man.")
    else:
        print("she is female.")

cries=Person(180,77,23)
maryam=Person(164,65,60)
recognaiz(maryam)
recognaiz(cries)