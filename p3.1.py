from sklearn.datasets import load_boston
data=load_boston()
#print(data)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(data.data,data.target)
#print(X_train,X_test,y_train,y_test)
from sklearn.linear_model import LinearRegression
clf=LinearRegression()
clf.fit(X_train,y_train)
predicted=clf.predict(X_test)
expexcted=y_test
import matplotlib.pyplot as plt
plt.figure(figsize=(4,3))
plt.scatter(expexcted,predicted)
plt.plot([0,50],[0,50],"--k")
plt.axis("tight")
plt.xlabel("True price ($1000s)")
plt.ylabel("Predicted price ($1000s)")
plt.tight_layout()
plt.show()