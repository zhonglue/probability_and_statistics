########################################################################
# Author: Zl Hu
# Date: 02/24/2020
# Description: the expectation of miner 
# A miner was unfortunately trapped in a mine with three exits
# First exit: walk 3 hours and can arrive a safety zone
# Second exit: walk 5 hours and return to the original point
# Third exit: walk 7 hours and return to the original point
# Now suppose this miner always randomly pick one of the exits
# What is the expected value of miner spent in this mine before he arrives the safety zone?
# 
# Answer: 15 hours
########################################################################


'''
茆诗松P202 题目
一矿工被困在有三个门的矿井里，第一个门通一坑道，3小时可达安全区；
第二门通一坑道，5小时又回到原处；
第三门通一坑道，7小时回到原处；
矿工总是等可能的在三个门中选一个，求他平均要多长时间才能到达安全区
答案为15小时
'''
import numpy as np 
from matplotlib import pyplot as plt 
from random import randint

iterations = 10000
x = np.arange(iterations)
y = np.zeros(iterations)

for i in range(iterations):
    result = 0
    while True:
        pick = randint(1,3)
        if pick == 1:
            result += 3
            break
        elif pick == 2:
            result += 5
        else:
            result += 7
    y[i]=result
print(sum(y)/iterations)
plt.scatter(x,y, s=0.1, color = 'g', marker = 'o')
plt.xlabel("Times of iterations")
plt.ylabel("Total time")
plt.style.use('seaborn')
plt.ylim(0, max(y))
plt.xlim(0, iterations)
plt.show()

'''
10000次循环之后，平均走出去的时间大概是14.92分钟，最多时间超过了150分钟
'''