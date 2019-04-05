import  pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
fig=plt.figure()
ax=fig.add_subplot(121)
ax.bar([1,2,3,4,5],[10,30,15,55,9] ,color="red")
ax.set(title="Frequency data chart",xlabel="numbers",ylabel="percent")
red_plot=mpatches.Patch(color="red",label="frequency")
plt.legend(handles=[red_plot])
plt.show()
plt.close()