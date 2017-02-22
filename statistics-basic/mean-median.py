# Mean & Median Customer Spend

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 20.0, 10000)

plt.hist(incomes, 50)
plt.show()

# calculate mean 
print np.mean(incomes)

# calculate median
print np.median(incomes)