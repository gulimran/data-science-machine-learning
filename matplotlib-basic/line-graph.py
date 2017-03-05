# MatPlotLib Basics

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Draw a line graph

x = np.arange(-3, 3, 0.001)

plt.plot(x, norm.pdf(x))
plt.show()
