import pandas as pd

data={'Name':['lena','carin','mery','allen'],'Family':['alex','jef','zakari','serkesyan'],'Age':[20,18,25,11]}
lst=["techer","friend","girl","boy"]
df=pd.DataFrame(data,index=lst)
print(df)
print("----------------------------------")
print(df.loc['friend'])
print("----------------------------------")
print(df['Name'])