########################################################################
# Author: Zl Hu
# Date: 02/24/2020
# Description: probability plot of normally distributed or uniformly distributed sample data
########################################################################


import numpy as np 
from matplotlib import pyplot as plt 
import math
import scipy.stats as st

np.random.seed(78952) # generate a fixed set of random number
# num = 50
num = 5000
x = np.random.uniform(80, 10, num)
x_int = x.astype(int)
print(x_int)

x_min, x_max = min(x_int), max(x_int)
bin_num = range(x_min, x_max, 2)
plt.hist(x, bins = bin_num, align = 'mid', alpha = 0.5, rwidth = 0.5)
plt.show()

data = sorted(x_int)
print(data)
z = np.zeros(num)
pi = math.pi
# Reverse function of CDF

ptiles = [(i+0.5)/num for i in range(num)]

z = st.norm.ppf(ptiles)
plt.style.use('seaborn')
# print((z, data))
plt.scatter(z, data)
plt.show()