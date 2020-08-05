# author: zhonglue
# date: 05/25
# Interval estimate: suppose samples follow normal distribution N(mu, 1)
# Denote the average of 10 samples as X-bar
# The probability of mu in [X-bar - 1, X-bar + 1] is approximately 95%
# Here, we verify this conclusion by setting mu as known (mu=0)
# Then we iterate the number


import random
import numpy as np 
from matplotlib import pyplot as plt 

mu, sigma, num = 0, 1, 10000
x = np.random.normal(mu, sigma, num)
iteration = 1000

plt.style.use('seaborn')
count = 0

for i in range(iteration):
    x = list(x)
    y = random.sample(x, 4)
    mean_y = np.mean(y)
    max_y = mean_y + 1
    
    min_y = mean_y - 1
    if abs(mean_y)>=1:
        count += 1
        plt.vlines(x=i, ymin=min_y, ymax = max_y, color = 'r')
        print(min_y, max_y)
    else:
        plt.vlines(x=i, ymin=min_y, ymax = max_y, color ='b')
ans = (iteration-count)/iteration

print("{:.5f}".format(ans))
print(count)
plt.xlim(0, iteration)
plt.ylim(-3,3)
plt.show()
