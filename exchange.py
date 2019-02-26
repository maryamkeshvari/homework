class Exchange:
    """we use this class for Exchange. """
    def __init__(self,convert):
        self.convert=convert
    def exchange_money(self,text_input):
        """in this method we convert doller to currency ."""
        dollar = int(input("How many dollars do you have to convert ? "))
        if "dram" in text_input:
            ratio =488.2

        elif "rial" in text_input:
            ratio = 14500

        elif "ruble" in text_input:
            ratio=65.53

        out_put= dollar*ratio
        print("your money is "+str(out_put)+" "+text_input+" .")
converts=["dram","rial","ruble"]

text_input = str(input("Please enter the currency you want : "))
while True:
    if text_input in converts:
        change = Exchange(converts)
        change.exchange_money(text_input)
    else:
        print("please enter other currency. ")
        text_input = str(input("Please enter the currency you want : "))
        change = Exchange(converts)
        change.exchange_money(text_input)
    break
