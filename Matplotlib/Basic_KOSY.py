import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10
points = 2*(xmax-xmin)
x = np.linspace(xmin, xmax, points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'black') # blue x axis
plt.plot([0,0],[ymin,ymax], 'black') # blue y axis

ax.set_xlabel("x values")
ax.set_ylabel("y values")
ax.set_title("Some Graph")
ax.grid(True)

ax.set_xticks(np.arange(xmin, xmax, 1))
ax.set_yticks(np.arange(ymin, ymax, 1))

plt.show()
