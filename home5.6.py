import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as mpatches


fig=plt.figure(figsize=(9,9))
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
ax1=fig.add_subplot(grid[:-1, 0])
ax2=fig.add_subplot(grid[-1, 1:])
ax3=fig.add_subplot(grid[0, 1:])

x = np.linspace(0, 2*np.pi, 100)
ax1.plot(np.sin(x), color='pink')
ax1.set(title="sin",xlabel='X',ylabel='Y' )
ax2.plot(np.cos(x),color='red')
ax2.set(xlabel="X",ylabel="Y",title="cos")
ax1_patch = mpatches.Patch(color='pink')
ax2_patch = mpatches.Patch(color='red')
ax3.plot(np.tan(x),color='green')
ax3.set(xlabel="X",ylabel="Y",title="tan")
ax3_patch = mpatches.Patch(color='green')

fig.legend([ax1_patch, ax2_patch,ax3_patch ],["sin", "cos","tan"],loc="upper left")

p=PdfPages('multipage.pdf')
p.savefig()
p.close()