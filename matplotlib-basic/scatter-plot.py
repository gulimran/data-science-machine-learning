# MatPlotLib Basics

from pylab import randn
import matplotlib.pyplot as plt

# Scatter Plot

X = randn(500)
Y = randn(500)

plt.scatter(X,Y)

plt.show()