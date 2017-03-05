# MatPlotLib Basics

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Mutiple Plots on One Graph
# Adjust the Axes

x = np.arange(-3, 3, 0.001)

axes = plt.axes()

axes.set_xlim([-5, 5])
axes.set_ylim([0, 1.0])

axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()
