class Exchange:
    """we use this class for Exchange. """
    def __init__(self,convert):
        self.convert=convert
    def exchange_sell(self,text_input):
        """in this method we convert doller to currency ."""

        dollar = int(input("How many dollars do you have to convert ? "))
        if "dram" or "Dram" in text_input:
            Rates = {1: 450, 2: 480, 3: 500, 4: 488, 5: 477, 6: 478, 7: 477,8:466,9:467,10:478,11:479,12:480,13:490,14:491,15:492,16:493,17:495,
                        18:493,19:469,20:489,21:469,22:499,23:493,24:460}
        elif "rial" or "Rial" in text_input:
            Rates = {1: 144500, 2: 144800, 3: 145000, 4: 144880, 5: 144770, 6: 144780, 7: 154770, 8: 144660, 9: 144670, 10: 144780, 11: 144790,
                       12: 144800, 13: 144900, 14: 144910, 15: 144920, 16: 144930, 17: 144950,
                       18: 144930, 19: 144690, 20: 144890, 21: 144690, 22: 144990, 23: 144930, 24: 144600}

        elif "ruble" or "Ruble" in text_input:
            Rates = {1: 50, 2: 80, 3: 40, 4: 88, 5: 77, 6: 48, 7: 77, 8: 66, 9: 67, 10: 78, 11: 79,
                       12: 80, 13: 90, 14: 91, 15: 92, 16: 100, 17: 95,
                       18: 93, 19:69, 20: 89, 21: 69, 22: 99, 23: 93, 24: 60}

        last_Rate=int(input("please enter rate when you buy dollars: "))
        Rate=int(input("please enter rate in this time: "))
        out_put1 = dollar * Rate
        print("your money is "+str(out_put1) + " but ")
        out_put= dollar*max(Rates.values())
        time=[key for m in [max(Rates.values())] for key,val in Rates.items() if val == m]
        if Rate<max(Rates.values()):
            print("your money is "+str(out_put)+" "+text_input+" at "+str(time) +" "+"o'clock. it is the best time for sell your dollar.")
            answer=str(input("Do you want to sell your dollars at the best time ? please enter your answer : "))
            if answer=="yes":
                difference=max(Rates.values())-last_Rate
                profits=dollar*difference
                if difference>0:
                    print(" Your profits is :" +str(profits))
                else:
                    print(" Your loss is :" +str(profits))
        else:
            ans=str(input("Do you want to sell your dollars now?? please enter your answer : "))
            if ans=="yes":
                difference=Rate-last_Rate
                profits=dollar*difference
                if difference>0:
                    print(" Your profits is :" +str(profits))
                else:
                    print(" Your loss is :" +str(profits))
            else:
                 print("If you change your mind, come back.")


converts=["dram","Dram","rial","Rial","ruble","Ruble"]

text_input = str(input("Please enter the currency you want : "))
while True:
    if text_input in converts:
        change = Exchange(converts)
        change.exchange_sell(text_input)
    else:
        print("please enter other currency. ")
        text_input = str(input("Please enter the currency you want : "))
        change = Exchange(converts)
        change.exchange_sell(text_input)
    break

