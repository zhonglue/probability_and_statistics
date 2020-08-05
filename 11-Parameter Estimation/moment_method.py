# author: zhonglue
# date: 05/17/2020
# moment method: estimate the parameter of uniform distribution through limited number of sample

import numpy as np 
from matplotlib import pyplot as plt 
import random
import math

num = 30
a = 0 
b = 1
z = np.random.uniform(0, 1, num)

z_mean = np.mean(z)
z_var = np.std(z)*(num-1)/num

ans_a = z_mean - math.sqrt(3)*z_var
ans_b = z_mean + math.sqrt(3)*z_var

# 怎么保留z的前三位小数？
# python的print好像不太好用
# print("{:.3f}".format(z)) Error
print(z, z_mean, z_var, ans_a, ans_b)
bins = np.arange(0,1.0, step=0.05)
plt.hist(z, bins, color = 'g')
plt.style.use('seaborn')
plt.show()