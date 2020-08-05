#######################################################################
# Author: Zl Hu
# Date: 05/16/20
# Descritpion: compare the t distribution with normal distribution
#######################################################################

import numpy as np 
from matplotlib import pyplot as plt 
import random
from scipy.stats import norm
import math

# set the seed number
np.random.seed(0)

mu, sigma, num = 172, 10, 100000
y = np.random.normal(mu, sigma, num) # generate 100000 normally distributed variables
y = list(y)
# print(y)
sample_num = 10
# random sampling: random.sample
iteration = 10000


# np.arange() is only integers?
# change to np.zeros() removes the problem
x = np.zeros(iteration)##
z = np.zeros(iteration)
q = np.arange(iteration)
for i in range(iteration):
    np.random.seed(987654321)
    # set the seed number so that every random number is same
    new_slice = random.sample(y, sample_num) #select 10 random samples
    # print(new_slice)
    slice_mean = np.mean(new_slice)
    slice_std = np.std(new_slice, ddof = 1) # calculate sample variance (div by n-1)
    # why x and z are all integers?
    # print(slice_std)
    x[i] = (slice_mean-mu)*math.sqrt(sample_num)/sigma*1.0  # normal distribution
    z[i] = (slice_mean-mu)*math.sqrt(sample_num)/slice_std*1.0 # t distribution
    # print(x[i], z[i])
    # for those outliers in t distribution, differ from the mean by more than 5 std variance, print the result
    # if abs(z[i]>5):
        # print(new_slice, slice_mean, slice_std)

plt.style.use('seaborn')

plt.scatter(q, x, alpha = 0.75, marker = '*', color = 'g')
plt.scatter(q, z, alpha = 0.75, marker = '.', color = 'r')
plt.xlim(0,iteration)
plt.show()
n, bins, patches = plt.hist(x, bins= 50, color='g', edgecolor = 'black', align = 'mid', density = 'True',
                            alpha=0.7, rwidth=0.85)
x_normal = np.linspace(min(x), max(x), 50)
print(x_normal)

# the x has normal distribution
y_normal = norm.pdf(x_normal, loc = 0, scale = 1)
plt.plot(x_normal, y_normal, 'r--')
plt.show()

n, bins, patches = plt.hist(z, bins= 'auto', color='r', edgecolor = 'black', align = 'mid', density = 'True',
                            alpha=0.7, rwidth=0.85)
plt.show()