#########################################################
#  Date: 07/26/2020
#  Author: ZL Hu
#   Verify the central limit theorem
#     Toss a dice 600 times, record the time where 3 is up
#     Repeat this process for 1000 times, the total number has a normal distribution with mean of 100, and variance of 600 sigma^2
##########################################################

import numpy as np 
from matplotlib import pyplot as plt 
from scipy.stats import norm
import math

iteration = 100000
num = 60

result = np.zeros(iteration)
for i in range(iteration):
    count = 0
    for j in range(num):
        x = np.random.randint(1, 7, 1)
        if x == 3:
            count += 1
    result[i] = count

result_min, result_max = min(result), max(result)
bin_num = np.arange(result_min, result_max, 1)
plt.hist(result, bins = bin_num, rwidth = 0.5, align = 'left', edgecolor = 'black', density='True')
x = np.linspace(0, 20, 50)
y = norm.pdf(x, loc = 10, scale = math.sqrt(50/6) )
plt.plot(x, y, 'r--')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.show()