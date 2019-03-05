class Regression:
    def __init__(self,time):
        self.time=time
    def calc_hour_year(self):
        day=365
        hour=24
        minute=60
        second=60
        hour_in_year=day*hour
        print("hour in one year is "+str(hour_in_year))
        minute_in_year = hour_in_year*minute
        print("minute in one year is " + str(minute_in_year))
        second_in_year = minute_in_year*second
        print("second in one year is " + str(second_in_year))

time=[]
times=Regression(time)
times.calc_hour_year()