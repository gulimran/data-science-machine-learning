# MatPlotLib Basics

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Mutiple Plots on One Graph
# Save it to a File

x = np.arange(-3, 3, 0.001)

plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()
plt.savefig('./MyPlot.png', format='png')