# Mode

import numpy as np
from scipy import stats

# generate some age data for 500 people
ages = np.random.randint(18, high=90, size=500)
print ages

# calculate mode
print stats.mode(ages)