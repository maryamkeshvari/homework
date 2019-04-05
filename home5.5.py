import pandas as pd
import numpy as np
#import matplotlib.pyplot.legend as legend
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(9,9))
#DATA={'City':['Tehran','Esfahan','Mashhasd','Shiraz'],'Crowded':[12000000,500000,4000000,3500000]}
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
ax1=fig.add_subplot(grid[:-1, 1:])
ax2=fig.add_subplot(grid[:-1, 0])
ax3=fig.add_subplot(grid[-1, 1:])
ax4=fig.add_subplot(grid[-1,0])
ax1.bar(['Tehran','Esfahan','Mashhasd','Shiraz'],[12000000,5000000,4000000,3500000], color='plum')
ax1.set(title="Population chart",xlabel='City',ylabel='Crowded' )
y=[2,3,4,8,9,11,33,44]
z=[25,3,42,55,9,11,33,44]
ax2.plot(y,z, color='orange')
ax2.set(title="frequency data",xlabel='y',ylabel='z' )
x = np.linspace(0, 2*np.pi, 100)
ax3.plot(np.cos(x),color='green')
ax3.set(xlabel="X",ylabel="Y",title="cos")
ax1_patch = mpatches.Patch(color='plum')
ax2_patch = mpatches.Patch(color='orange')
ax3_patch = mpatches.Patch(color='green')
ax4_patch = mpatches.Patch(color='red')
ax4.scatter([3,12,2,4,7,9,5,11],[22,14,23,17,10,9,22,2],color="red")
ax4.set(xlabel="X",ylabel="Y",title="scatter")
fig.legend([ax1_patch, ax2_patch, ax3_patch,ax4_patch],["pupulation", "frequency", "cos","number"],loc="upper right")
plt.show()
plt.close()