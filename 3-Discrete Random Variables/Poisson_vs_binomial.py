###########################################################################
# Author: ZL Hu
# Date: 02/20/2020
# Description: Compare the Poisson distribution and Binomial distribution
#  for a binomial distribution, when the n is large, p is relatively small, the binomial distribution 
#  can be approximated using Poisson distribution
###########################################################################


import numpy as np 
from matplotlib import pyplot as plt 
import math

# compare whether Poisson ratio is a good proximity of Binomial distribution

number = 100
prob = 0.2
lamda = number*prob

x = np.arange(number)
y_binomial = np.zeros(number)
z_poisson = np.zeros(number)

for i in range(number):
    y_binomial[i] = math.factorial(number)/(math.factorial(number-i)*math.factorial(i))*(prob)**i*(1-prob)**(number-i)       # For binomial distribution, P(X=i) = Cni p^i(1-p)^i
    z_poisson[i] = lamda**i*np.exp(-lamda)/math.factorial(i)  # for poisson distribution, P(X=i)=lambda^i/i! * exp(-lambda), here, lambda = n * p

plt.style.use('seaborn') # use a nice style
plt.rc('font', size =14)
plt.rc('figure', titlesize = 18)
plt.rc('axes', labelsize =15)
plt.rc('axes', titlesize =18)

plt.title("Poisson distribution vs Binomial distribution")
plt.xlabel("Number")
plt.ylabel("Probability")
plt.xlim(0, 100)
plt.scatter(x, y_binomial, color = 'g', marker = 'o', alpha = 0.5)
plt.scatter(x, z_poisson, color= 'b', marker = '*', alpha = 0.5)
plt.show()