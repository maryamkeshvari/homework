import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
col_names = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target']
heart_df=pd.read_csv("heart.csv",header=None,names=col_names,skiprows=1)
fig=plt.figure(figsize=(20,20))
ax=sn.pairplot(data=heart_df)
plt.show()
plt.close()
