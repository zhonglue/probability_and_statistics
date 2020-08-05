########################################################################
# Author: Zl Hu
# Date: 02/24/2020
# Description: plot the chi-squared distribution
########################################################################


import numpy as np 
from matplotlib import pyplot as plt 
import random
import statistics as st 

num = 10000
z = np.zeros(num)
k = 100
mu, sigma = 0, 1
for i in range(k):
    y =  np.random.normal(mu, sigma, num)   # 生成拥有10000个样本的标准正态分布
    y = y**2 # 标准正态分布平方
    z = z + y # 标准正态分布平方和

n, bins, patches = plt.hist(x=z, bins='auto', color='#0504aa',  # 绘制直方图
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
maxfreq = n.max()
plt.style.use('seaborn')
plt.show()
