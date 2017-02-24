# Poisson Probability Mass Function

# My website gets on average 500 visits per day. 
# What's the odds of getting 550?

from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt

mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))
plt.show()