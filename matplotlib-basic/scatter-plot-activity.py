# -*- coding: utf-8 -*-
# MatPlotLib Basics

from pylab import randn
import matplotlib.pyplot as plt
import numpy as np

# Scatter Plot

X = np.random.normal(3.0, 1.0, 1000)
Y = np.random.normal(50.0, 1.0, 1000)

axes = plt.axes()

axes.set_xlim([0, 24])
axes.set_ylim([0, 100])

plt.xlabel('time spent watching tv')
plt.ylabel('my age')

plt.scatter(X,Y)

plt.show()