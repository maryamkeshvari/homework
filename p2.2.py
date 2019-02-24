class Student:
    def __init__(self,diligence,responsibility,background):
        self.diligence=diligence
        self.responsibility=responsibility
        self.background=background
def scores(student):

    score=(student.diligence+student.responsibility+student.background)/3
    print(score)
student=Student(50,90,40)
scores(student)