# Mean, Median, Mode

# compute the median - since we have a nice, even distribution 
# it should be close to 27,000
# income data, centered around 27,000 with a normal distribution and 
# standard deviation of 15,000, with 10,000 data points.

import numpy as np

incomes = np.random.normal(27000, 15000, 10000)
print np.median(incomes)

# Now we'll add a billionaire into the mix to highlight income inequality
incomes = np.append(incomes, [1000000000])

# The median won't change much, but the mean does
print np.median(incomes)
print np.mean(incomes)
