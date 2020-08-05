#########################################################
#  Date: 07/26/2020
#  Author: ZL Hu
#   Verify the central limit theorem
#     The summation of 100 uniformly distributed variables (0, 1)
#     has normal distribution with mu = 50, sigma = sqrt(25/6)
##########################################################

import numpy as np 
from matplotlib import pyplot as plt 
from scipy.stats import norm
import math


iteration = 100000
num = 100

result = np.zeros(iteration)

for i in range(iteration):
    x = 0
    for j in range(num):
        x += np.random.uniform(0, 1)
    result[i] = x

result_min, result_max = min(result), max(result)
bin_num = np.arange(result_min, result_max, 1)
plt.hist(result, bins = bin_num, rwidth = 0.5, align = 'mid', edgecolor = 'black', density='True')
x = np.linspace(30, 70, 100)
y = norm.pdf(x, loc = 50, scale = math.sqrt(50/6) )
plt.plot(x, y, 'r--')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.show()
