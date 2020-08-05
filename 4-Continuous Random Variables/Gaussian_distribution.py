###########################################################################
# Author: Zl Hu
# Date: 02/24/2020
# Description: Draw the plot of gaussion distribution with different lambda and sigma
# 
# Note: there are many other ways (perhaps simpler ways) to plot, such as using the scipy.stats.norm 
############################################################################



import numpy as np 
from matplotlib import pyplot as plt 
import math

lambda_1 = 50
lambda_2 = -1
lambda_3 = 1


# lambda_2 = 1
# lambda_3 = 3

# sigma can not be 0
#sigma = 1 

sigma_1 = 1
#sigma_2 = 0.5
#sigma_3 = 2

pi = math.pi 
print(pi)
x = np.arange(-5, 5, 0.01)
y_1 = 1/(math.sqrt(2*pi)*sigma_1)*np.exp(-(x-lambda_1)**2/2/sigma_1**2)
y_2 = 1/(math.sqrt(2*pi)*sigma_1)*np.exp(-(x-lambda_2)**2/2/sigma_1**2)
y_3 = 1/(math.sqrt(2*pi)*sigma_1)*np.exp(-(x-lambda_3)**2/2/sigma_1**2)

plt.style.use('seaborn')
plt.plot(x, y_1)
plt.plot(x, y_2)
plt.plot(x, y_3)

# plt.ylim(0, 0.5)
plt.show()