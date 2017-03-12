# Covariance

# Covariance measures how two variables vary in tandem from their means.
# An e-commerce company interested in finding a correlation between page speed 
# (how fast each web page renders for a customer) and how much a customer spends.
# numpy offers covariance methods, but we'll do it the "hard way" to show 
# what happens under the hood. Basically we treat each variable as a vector of 
# deviations from the mean, and compute the "dot product" of both vectors. 
# Geometrically this can be thought of as the angle between the two vectors in 
# a high-dimensional space, but you can just think of it as a measure of 
# similarity between the two variables.

# Make purchase amounts a function of page speed, making a very real 
# correlation. The negative value indicates an inverse relationship; 
# pages that render in less time result in more money spent.

# Covariance is sensitive to the units used in the variables, which makes 
# it difficult to interpret. Correlation normalizes everything by their 
# standard deviations, giving you an easier to understand value that 
# ranges from -1 (for a perfect inverse correlation) to 
# 1 (for a perfect positive correlation)

import numpy as np
from pylab import *

def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]
    
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)
    
def correlation(x, y):
    stddevx = x.std()
    stddevy = y.std()
    return covariance(x,y) / stddevx / stddevy  # check for divide by zero here
    
pageSpeeds = np.random.normal(3.0, 1.0, 1000)

purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)

show()

print covariance (pageSpeeds, purchaseAmount)

print correlation(pageSpeeds, purchaseAmount)