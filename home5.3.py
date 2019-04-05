import pandas as pd

data={'Name':['lena','carin','mery','allen'],'Family':['alex','jef','zakari','serkesyan'],'Age':[20,18,25,11]}
lst=["techer","friend","girl","boy"]
df=pd.DataFrame(data,index=lst)

df.to_csv("E:/dar30/master/AI/home5.3.csv")
print(df)
print("----------------------------------------")
df2=pd.read_csv("E:/dar30/master/AI/home5.3.csv",sep=",")
print(df2)