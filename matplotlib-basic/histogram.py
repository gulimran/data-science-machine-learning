# MatPlotLib Basics

import matplotlib.pyplot as plt
import numpy as np

# Histogram

incomes = np.random.normal(27000, 15000, 10000)

plt.hist(incomes, 50)
plt.show()