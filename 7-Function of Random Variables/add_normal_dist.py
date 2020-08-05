###########################################################
#  Date: 07/21/2020
#  Author: ZL Hu
#   addition of two normal distributions
###########################################################

import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib import mlab
from scipy.stats import norm
import math

num = 10000

# x = np.random.normal(0, 1, num)
# y = np.random.normal(0, 1, num)

# z = x + y
# num_bins = 50
# n, bins, patches = plt.hist(z, num_bins, histtype = 'bar', density = 'True', facecolor = 'yellowgreen', alpha = 0.75, edgecolor = 'black')
# y = norm.pdf(bins, 0, math.sqrt(2))

# plt.plot(bins, y)
# plt.style.use('seaborn')
# plt.show()
z = np.random.normal(4, 1, num)
for i in range(10):
    z += np.random.normal(4, 1, num)
num_bins = 50
n, bins, patches = plt.hist(z, num_bins, density = 1, histtype = 'bar', facecolor = 'yellowgreen', edgecolor = 'black' )
y = norm.pdf(bins, 44, math.sqrt(10))
plt.plot(bins, y)
plt.style.use('seaborn')
plt.show()