#########################################################################################
#  Date: 07/18/2020
#  Author: ZL Hu
#  Description: derived distribution
#   X is randomly distributed between 60-90, Y = 180/X, what is the distribution of Y?
#  
#  Analytical solution: f(y)=6/y^2
#########################################################################################

import numpy as np 
from matplotlib import pyplot as plt 

num = 100000
x = np.random.uniform(60, 90, num)

x_min, x_max = min(x), max(x)
bin_num = int(abs(x_max - x_min))

plt.style.use('seaborn')
plt.hist(x, bins = bin_num, alpha = 0.5, align = 'mid', rwidth = 0.5)
plt.show()
y = [180/i for i in x]
# print(y)

y_min, y_max = min(y), max(y)
bin_num = int(abs(y_max - y_min)/0.05)
plt.hist(y, bins = bin_num, alpha = 0.5, align = 'left', rwidth = 0.2 )
plt.show()