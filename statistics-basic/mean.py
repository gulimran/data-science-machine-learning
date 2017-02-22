# Mean, Median, Mode

# compute the mean (average)
# income data, centered around 27,000 with a normal distribution and 
# standard deviation of 15,000, with 10,000 data points.
# matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(27000, 15000, 10000)
print np.mean(incomes)

plt.hist(incomes, 50)
plt.show()