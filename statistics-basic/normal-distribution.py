# normal distribution
# Generate some random numbers with a normal distribution. 
# "mu" is the desired mean, 
# "sigma" is the standard deviation

import numpy as np
import matplotlib.pyplot as plt

mu = 5.0
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)
plt.hist(values, 50)
plt.show()