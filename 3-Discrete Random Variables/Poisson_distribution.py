# Poisson distribution
# Author: Zhonglue Hu
# Date: Feb 20, 2020

import numpy as np 
from matplotlib import pyplot as plt 
import math

# Set the parameters

number = 100 # Total number of tests  
lamda = 10 # the poisson ratio

x = np.arange(number)
z_poisson = np.zeros(number)

for i in range(number):
    z_poisson[i] = lamda**i*np.exp(-lamda)/math.factorial(i)

plt.style.use('seaborn') # use a nice style
plt.rc('font', size =14)
plt.rc('figure', titlesize = 18)
plt.rc('axes', labelsize =15)
plt.rc('axes', titlesize =18)

plt.title("Poisson distribution vs Binomial distribution")
plt.xlabel("Number")
plt.ylabel("Probability")
plt.xlim(0,100)
plt.ylim(0, 0.15)
plt.scatter(x, z_poisson, color= 'r', marker = 'o', alpha = 0.5)
plt.show()