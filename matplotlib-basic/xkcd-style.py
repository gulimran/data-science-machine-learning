# MatPlotLib Basics

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# XKCD Style

plt.xkcd()

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.xticks([])
plt.yticks([])

ax.set_ylim([-30, 10])

data = np.ones(100)
data[70:] -= np.arange(30)

plt.annotate('THE DAY I REALIZED\nI COULD EAT ANYTHING\nWHENEVER I WANTED',
              xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))
    
plt.plot(data)

plt.xlabel('time')
plt.ylabel('my overall health')

plt.show()