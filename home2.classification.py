class Classification:
    def __init__(self,blood,number):
        self.blood=blood
        self.number=number
    def blood_gp(self):
        positive_gp = [item for item in blood_grupe if "+" in item]
        print("positive blood groups =  "+str(positive_gp))
        AB_gp=[item for item in blood_grupe if "AB" in item]
        print("all AB = "+str(AB_gp))
        negative_gp = [item for item in blood_grupe if "-" in item]
        print("negative blood groups = "+str(negative_gp))
        o_gp=[item for item in blood_grupe if "O" in item]
        print("all O blood groups = "+str(o_gp))
    def numbers(self):
        odd=[number for number in numbers if number%2==1]
        print("Odd numbers = "+str(odd))
        even=[number for number in numbers if number%2==0]
        print("Even number = "+str(even))


numbers=[1,2,4,6,8,9,11,13,17,18]
blood_grupe=["+A","+AB","-O","-B","-A","+AB","-O","+B","+O"]
blood=Classification(blood_grupe,numbers)
blood.blood_gp()
num=Classification(blood_grupe,numbers)
num.numbers()