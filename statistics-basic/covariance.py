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

# Here page speed and purchase amount totally random and independent of 
# each other; a very small covariance will result as there is no real correlation


import numpy as np
from pylab import *

def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]
    
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)
    
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000)

scatter(pageSpeeds, purchaseAmount)

show()

print covariance (pageSpeeds, purchaseAmount)