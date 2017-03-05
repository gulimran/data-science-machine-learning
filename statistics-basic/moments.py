# moments
# It is the quantitative measures of the shape of the probability distribution
# function.  The first moment is the mean.  The second moment is the variance.
# The third moment is skew - how lopsided is the distribution.  A distribution
# with longer tail on the left will be skewed left and have negative skew.
# The fourth moment is kurtosis, which describes the shape of the tail.  How
# thick is the tail and how sharp is the peak, compared to a normal distribution.
# Higher peaks have higher kurtosis.

import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt

# normal-distributed random set of data:
vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 50)
plt.show()

# The first moment is the mean; this data should average out to about 0:
print np.mean(vals)

# The second moment is the variance:
print np.var(vals)

# The third moment is skew - since our data is centered around 0, 
# it should be almost 0:
print sp.skew(vals)

# The fourth moment is "kurtosis", which describes the shape of the tail. 
# For a normal distribution, this is 0:
print sp.kurtosis(vals)