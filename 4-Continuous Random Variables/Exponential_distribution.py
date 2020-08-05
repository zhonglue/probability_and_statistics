########################################################################
# Author: Zl Hu
# Date: 02/24/2020
# Description: plot the exponential distribution with different lambda value
########################################################################

import numpy as np 
from matplotlib import pyplot as plt 
import math


x = np.arange(0.001, 5, 0.001)
lamda_1 = 0.5
lamda_2 = 1
lamda_3 = 3


# this is the density function of exponential distribution
'''
y_1 = lamda_1*np.exp(-lamda_1 * x)
y_2 = lamda_2*np.exp(-lamda_2 * x)
y_3 = lamda_3*np.exp(-lamda_3 * x)
'''

# this is the distribution function of exponential distribution
y_1 = 1 - np.exp(-lamda_1 * x)
y_2 = 1 - np.exp(-lamda_2 * x)
y_3 = 1 - np.exp(-lamda_3 * x)

plt.style.use('seaborn')
plt.plot(x, y_1, 'r')
plt.plot(x, y_2, 'g')
plt.plot(x, y_3, 'b')

plt.xlim(0, 5)
plt.ylim(0, 1)

plt.show()