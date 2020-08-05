################################################################
# Author: ZL Hu
# Date: 02/20/2020
# Description: Draw the plot of binomial distribution
################################################################

import numpy as np 
from matplotlib import pyplot as plt 
import math

# set the parameter
number = 100 # number of tests
prob_1 = 0.5 # probability of Event A happens
#prob_2 = 0.75
#prob_3 = 0.5
#prob_4 = 0.25

x = np.arange(number) # initialize X
y_binomial_1 = np.zeros(number) # initialize Y
#y_binomial_2 = np.zeros(number)
#y_binomial_3 = np.zeros(number)
#y_binomial_4 = np.zeros(number)

for i in range(number):
    y_binomial_1[i] = math.factorial(number)/(math.factorial(number-i)*math.factorial(i))*(prob_1)**i*(1-prob_1)**(number-i)       # For binomial distribution, P(X=i) = Cni p^i(1-p)^i
 #   y_binomial_2[i] = math.factorial(number)/(math.factorial(number-i)*math.factorial(i))*(prob_2)**i*(1-prob_2)**(number-i)       # For binomial distribution, P(X=i) = Cni p^i(1-p)^i
 #   y_binomial_3[i] = math.factorial(number)/(math.factorial(number-i)*math.factorial(i))*(prob_3)**i*(1-prob_3)**(number-i)       # For binomial distribution, P(X=i) = Cni p^i(1-p)^i
 #   y_binomial_4[i] = math.factorial(number)/(math.factorial(number-i)*math.factorial(i))*(prob_4)**i*(1-prob_4)**(number-i)

plt.style.use('seaborn') # use a nice style
plt.rc('font', size =14)
plt.rc('figure', titlesize = 18)
plt.rc('axes', labelsize =15)
plt.rc('axes', titlesize =18)

plt.title("Binomial distribution")
plt.xlabel("Number")
plt.ylabel("Probability")
plt.xlim(0, 100)
#plt.ylim(0, 0.1)
plt.scatter(x, y_binomial_1, alpha = 0.5)
#plt.scatter(x, y_binomial_2, alpha = 0.5)
#plt.scatter(x, y_binomial_3, alpha = 0.5)
#plt.scatter(x, y_binomial_4, alpha = 0.5)

plt.show()