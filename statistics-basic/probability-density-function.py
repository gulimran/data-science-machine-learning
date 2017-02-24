# Normal / Gaussian
# Visualize the probability density function

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3, 3, 0.001)
plt.plot(x, norm.pdf(x))
plt.show()