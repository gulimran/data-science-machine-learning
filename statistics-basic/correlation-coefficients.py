# Covariance

# Covariance measures how two variables vary in tandem from their means.
# An e-commerce company interested in finding a correlation between page speed 
# (how fast each web page renders for a customer) and how much a customer spends.
# numpy offers covariance methods.

# Make purchase amounts a function of page speed, making a very real 
# correlation. The negative value indicates an inverse relationship; 
# pages that render in less time result in more money spent.

# Covariance is sensitive to the units used in the variables, which makes 
# it difficult to interpret. Correlation normalizes everything by their 
# standard deviations, giving you an easier to understand value that 
# ranges from -1 (for a perfect inverse correlation) to 
# 1 (for a perfect positive correlation)

# numpy can do all this with numpy.corrcoef. It returns a matrix of the correlation 
# coefficients between every combination of the arrays passed in

import numpy as np
from pylab import *
    
pageSpeeds = np.random.normal(3.0, 1.0, 1000)

purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)

show()

print np.corrcoef(pageSpeeds, purchaseAmount)
