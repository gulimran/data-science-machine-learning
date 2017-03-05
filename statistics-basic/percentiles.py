# percentiles
# In a data set, the point at which X% of the values are less than that value X

import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 50)
plt.show()

# 50th percentile is same as median
print np.percentile(vals, 50)

# get 90th percentile
print np.percentile(vals, 90)

# get 20th percentile
print np.percentile(vals, 20)